from src.IR.instructions import *
from src.IR.temp_manager import TempManager
from src.AST.Karkas import MatchCase, DefaultCase

class NASMGenerator:
    def __init__(self):
        self.lines = []
        self.temp_manager = TempManager()
        self.label_counter = 0
        self.arg_registers = ["rdi", "rsi", "rdx", "rcx", "r8", "r9"]
        self.func_params = {}
        self.string_literals = {}
        self.string_counter = 0
        self.defined_labels = set()
        self.defined_functions = set()

    def generate(self, instructions):
        self.lines = []
        self.label_counter = 0
        self.string_literals = {}
        self.defined_labels = set()
        self.defined_functions = set()

        self.emit("section .data")
        self.emit('newline db 10, 0')
        self.emit('format db "%d", 10, 0')
        self.emit('format_str db "%s", 10, 0')
        self.emit('True dq 1')
        self.emit('False dq 0')
        self.collect_variables(instructions)
        self.emit_string_literals()

        self.emit("\nsection .text")
        self.emit("extern printf")
        self.emit("extern getchar")
        self.emit("global _start")

        for instr in instructions:
            if isinstance(instr, IRFunctionStart) and instr.name != "func_main":
                self.translate(instr)

        self.emit("_start:")
        for instr in instructions:
            if not isinstance(instr, IRFunctionStart) or instr.name == "func_main":
                self.translate(instr)

        self.emit("; Wait for key press before exit")
        self.emit("call getchar")
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
        skip_prefixes = ("case_", "default_case", "end_match", "else_", "endif_", "while_", "for_", "try_", "catch_", "end_try")
        func_names = {instr.name for instr in instructions if isinstance(instr, IRFunctionStart)}
        for instr in instructions:
            for attr in vars(instr).values():
                if isinstance(attr, str) and attr.isidentifier():
                    if any(attr.startswith(p) for p in skip_prefixes):
                        continue
                    if attr in func_names:
                        continue
                    if attr not in seen:
                        self.emit(f"{attr} dq 0")
                        seen.add(attr)

    def resolve_value(self, val):
        if isinstance(val, str):
            if val.startswith('"') and val.endswith('"'):
                name = f"str_{self.string_counter}"
                self.string_counter += 1
                self.string_literals[name] = val.strip('"')
                return f"rel {name}"
            elif not val.isnumeric():
                return f"qword [rel {val}]"
        return str(val)

    def translate(self, instr):
        if isinstance(instr, IRFunctionStart):
            if instr.name in self.defined_functions:
                return
            self.defined_functions.add(instr.name)
            self.func_params[instr.name] = instr.params
            self.emit(f"{instr.name}:")
            self.emit("push rbp")
            self.emit("mov rbp, rsp")
            for i, param in enumerate(instr.params):
                if i < len(self.arg_registers):
                    self.emit(f"mov qword [rel {param}], {self.arg_registers[i]}")
                else:
                    offset = 16 + 8 * (i - len(self.arg_registers))
                    self.emit(f"mov rax, [rbp+{offset}]")
                    self.emit(f"mov qword [rel {param}], rax")

        elif isinstance(instr, IRFunctionEnd):
            self.emit("pop rbp")
            self.emit("ret")

        elif isinstance(instr, IRAssign):
            self.emit(f"mov rax, {self.resolve_value(instr.value)}")
            self.emit(f"mov qword [rel {instr.target}], rax")

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
                self.emit(f"mov qword [rel {instr.result}], rax")
            elif instr.op in cmps:
                self.emit(f"cmp rax, {self.resolve_value(instr.right)}")
                self.emit(f"{cmps[instr.op]} al")
                self.emit("movzx rax, al")
                self.emit(f"mov qword [rel {instr.result}], rax")
            elif instr.op in {"&&", "||"}:
                self.translate_logical(instr)

        elif isinstance(instr, IRUnary):
            if instr.op == "!":
                self.emit(f"mov rax, {self.resolve_value(instr.operand)}")
                self.emit("cmp rax, 0")
                self.emit("sete al")
                self.emit("movzx rax, al")
                self.emit(f"mov qword [rel {instr.result}], rax")

        elif isinstance(instr, IRPrint):
            val = self.resolve_value(instr.value)
            if val.startswith("rel str_"):
                self.emit(f"mov rsi, {val}")
                self.emit("mov rdi, format_str")
            else:
                self.emit(f"mov rsi, {val}")
                self.emit("mov rdi, format")
            self.emit("xor rax, rax")
            self.emit("call printf")

        elif isinstance(instr, IRGoto):
            self.emit(f"jmp {instr.label}")

        elif isinstance(instr, IRIfGoto):
            cond = instr.condition
            if isinstance(cond, str) and cond.startswith("!"):
                real_cond = cond[1:]
                self.emit(f"mov rax, {self.resolve_value(real_cond)}")
                self.emit("cmp rax, 0")
                self.emit(f"je {instr.label}")
            else:
                self.emit(f"mov rax, {self.resolve_value(cond)}")
                self.emit("cmp rax, 0")
                self.emit(f"jne {instr.label}")

        elif isinstance(instr, IRLabel):
            if instr.label in self.defined_labels:
                return
            self.defined_labels.add(instr.label)
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
            self.emit(f"mov qword [rel {instr.target}], rax")

        elif isinstance(instr, IRReturn):
            self.emit(f"mov rax, {self.resolve_value(instr.value)}")
            self.emit("pop rbp")
            self.emit("ret")

        elif isinstance(instr, IRTryCatch):
            self.emit("; try/catch not supported in NASM runtime")

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
        self.emit("cmp rax, 0")
        if instr.op == "&&":
            self.emit("sete al")
        else:
            self.emit("setne al")
        self.emit("movzx rbx, al")
        self.emit(f"mov rax, {self.resolve_value(instr.right)}")
        self.emit("cmp rax, 0")
        if instr.op == "&&":
            self.emit("sete al")
            self.emit("movzx rax, al")
            self.emit("and rax, rbx")
        else:
            self.emit("setne al")
            self.emit("movzx rax, al")
            self.emit("or rax, rbx")
        self.emit(f"mov qword [rel {instr.result}], rax")
