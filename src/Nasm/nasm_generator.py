from src.IR.instructions import *
from src.IR.temp_manager import TempManager
from src.AST.Karkas import MatchCase, DefaultCase


class NASMGenerator:
    def __init__(self):
        self.lines = []
        self.data_section = set()
        self.temp_manager = TempManager()
        self.label_counter = 0
        self.arg_registers = ["rdi", "rsi", "rdx", "rcx", "r8", "r9"]
        self.func_params = {}
        self.string_literals = {}
        self.string_counter = 0

    def generate(self, instructions):
        self.lines = []
        self.data_section = set()
        self.label_counter = 0
        self.string_literals = {}

        self.emit("section .data")
        self.emit('newline db 10, 0')
        self.emit('format db "%d", 10, 0')
        self.emit('True dq 1')
        self.emit('False dq 0')
        self.collect_variables(instructions)
        self.emit_string_literals()

        self.emit("\nsection .text")
        self.emit("extern printf")
        self.emit("global _start")
        self.emit("_start:")

        for instr in instructions:
            self.translate(instr)

        self.emit("; Exit syscall")
        self.emit("mov rax, 60")
        self.emit("xor rdi, rdi")
        self.emit("syscall")

        return "\n".join(self.lines)

    def emit(self, line):
        self.lines.append(line)

    def emit_string_literals(self):
        for name, text in self.string_literals.items():
            escaped = text.encode('unicode_escape').decode().replace('"', '')
            self.emit(f'{name} db "{escaped}", 0')

    def collect_variables(self, instructions):
        seen = set()
        for instr in instructions:
            for attr in vars(instr).values():
                if (
                        isinstance(attr, str)
                        and attr.isidentifier()
                        and not attr.startswith("func_")
                        and attr not in seen
                ):
                    self.emit(f"{attr} dq 0")
                    seen.add(attr)

    def resolve_value(self, val):
        if isinstance(val, str):
            if val.startswith('"') and val.endswith('"'):
                name = f"str_{self.string_counter}"
                self.string_counter += 1
                self.string_literals[name] = val.strip('"')
                return name
            elif not val.isnumeric():
                return f"qword [{val}]"
        return str(val)

    def get_label(self, base):
        label = f"{base}_{self.label_counter}"
        self.label_counter += 1
        return label

    def translate(self, instr):
        if isinstance(instr, IRFunctionStart):
            self.func_params[instr.name] = instr.params
            self.emit(f"{instr.name}:")
            self.emit("push rbp")
            self.emit("mov rbp, rsp")
            for i, param in enumerate(instr.params):
                if i < len(self.arg_registers):
                    self.emit(f"mov qword [{param}], {self.arg_registers[i]}")
                else:
                    offset = 16 + 8 * (i - len(self.arg_registers))
                    self.emit(f"mov rax, [rbp+{offset}]")
                    self.emit(f"mov qword [{param}], rax")

        elif isinstance(instr, IRFunctionEnd):
            self.emit("pop rbp")
            self.emit("ret")

        elif isinstance(instr, IRAssign):
            self.emit(f"mov rax, {self.resolve_value(instr.value)}")
            self.emit(f"mov qword [{instr.target}], rax")

        elif isinstance(instr, IRBinary):
            self.emit(f"mov rax, {self.resolve_value(instr.left)}")
            ops = {"+": "add", "-": "sub", "*": "imul", "/": "idiv"}
            cmps = {"<": "setl", ">": "setg", "==": "sete", "!=": "setne"}
            if instr.op in ops:
                if instr.op == "/":
                    self.emit("cqo")
                    self.emit(f"mov rbx, {self.resolve_value(instr.right)}")
                    self.emit("idiv rbx")
                else:
                    self.emit(f"{ops[instr.op]} rax, {self.resolve_value(instr.right)}")
                self.emit(f"mov qword [{instr.result}], rax")
            elif instr.op in cmps:
                self.emit(f"cmp rax, {self.resolve_value(instr.right)}")
                self.emit(f"{cmps[instr.op]} al")
                self.emit("movzx rax, al")
                self.emit(f"mov qword [{instr.result}], rax")
            elif instr.op in {"&&", "||"}:
                self.translate_logical(instr)

        elif isinstance(instr, IRUnary):
            if instr.op == "!":
                self.emit(f"mov rax, {self.resolve_value(instr.operand)}")
                self.emit("cmp rax, 0")
                self.emit("sete al")
                self.emit("movzx rax, al")
                self.emit(f"mov qword [{instr.result}], rax")

        elif isinstance(instr, IRPrint):
            val = self.resolve_value(instr.value)
            if val.startswith("str_"):
                self.emit(f"mov rdi, {val}")
                self.emit("xor rax, rax")
            else:
                self.emit(f"mov rsi, {val}")
                self.emit("mov rdi, format")
                self.emit("xor rax, rax")
            self.emit("call printf")

        elif isinstance(instr, IRGoto):
            self.emit(f"jmp {instr.label}")

        elif isinstance(instr, IRIfGoto):
            self.emit(f"mov rax, {self.resolve_value(instr.condition)}")
            self.emit("cmp rax, 0")
            self.emit(f"jne {instr.label}")

        elif isinstance(instr, IRLabel):
            self.emit(f"{instr.label}:")

        elif isinstance(instr, IRCall):
            for i, arg in enumerate(instr.args):
                if i < len(self.arg_registers):
                    self.emit(f"mov {self.arg_registers[i]}, {self.resolve_value(arg)}")
                else:
                    self.emit(f"push {self.resolve_value(arg)}")
            self.emit(f"call {instr.name}")
            if len(instr.args) > len(self.arg_registers):
                self.emit(f"add rsp, {8 * (len(instr.args) - len(self.arg_registers))}")
            self.emit(f"mov qword [{instr.target}], rax")

        elif isinstance(instr, IRReturn):
            self.emit(f"mov rax, {self.resolve_value(instr.value)}")
            self.emit("pop rbp")
            self.emit("ret")

        elif isinstance(instr, IRTryCatch):
            try_label = self.get_label("try")
            catch_label = self.get_label("catch")
            end_label = self.get_label("end_try")
            self.emit(f"{try_label}:")
            for i in instr.try_block:
                self.translate(i)
            self.emit(f"jmp {end_label}")
            self.emit(f"{catch_label}:")
            for i in instr.catch_block:
                self.translate(i)
            self.emit(f"{end_label}:")

        elif isinstance(instr, MatchCase):
            self.emit(f"{instr.label}:")
            for stmt in instr.body:
                self.translate(stmt)
            self.emit(f"jmp {instr.end_label}")

        elif isinstance(instr, DefaultCase):
            self.emit(f"{instr.label}:")
            for stmt in instr.body:
                self.translate(stmt)
            self.emit(f"{instr.end_label}:")

    def translate_logical(self, instr):
        if instr.op == "&&":
            self.emit("cmp rax, 0")
            self.emit("sete al")
            self.emit("movzx rbx, al")
            self.emit(f"mov rax, {self.resolve_value(instr.right)}")
            self.emit("cmp rax, 0")
            self.emit("sete al")
            self.emit("movzx rax, al")
            self.emit("and rax, rbx")
            self.emit(f"mov qword [{instr.result}], rax")
        elif instr.op == "||":
            self.emit("cmp rax, 0")
            self.emit("setne al")
            self.emit("movzx rbx, al")
            self.emit(f"mov rax, {self.resolve_value(instr.right)}")
            self.emit("cmp rax, 0")
            self.emit("setne al")
            self.emit("movzx rax, al")
            self.emit("or rax, rbx")
            self.emit(f"mov qword [{instr.result}], rax")
