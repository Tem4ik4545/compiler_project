from src.IR.instructions import *
from src.IR.temp_manager import TempManager
from src.AST.Karkas import MatchCase, DefaultCase

class NASMGenerator:
    def __init__(self):
        self.lines = []
        self.label_counter = 0
        self.arg_registers = ["rdi", "rsi", "rdx", "rcx", "r8", "r9"]
        self.func_params = {}
        self.string_literals = {}
        self.string_counter = 0
        self.defined_labels = set()
        self.defined_functions = set()

    def generate(self, instructions):
        self.lines = []
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
        self.extract_string_literals(instructions)
        self.emit_string_literals()

        self.emit("\nsection .text")
        self.emit("extern printf")
        self.emit("extern getchar")
        self.emit("global _start")

        for instr in instructions:
            if isinstance(instr, IRFunctionStart) and instr.name != "func_main":
                self.translate(instr)

        self.emit("_start:")

        # вызываем последнюю пользовательскую функцию (не main, не _start)
        last_func = None
        for instr in reversed(instructions):
            if isinstance(instr, IRFunctionStart) and instr.name not in {"_start", "func_main"}:
                last_func = instr
                break

        if last_func:
            for i, arg in enumerate(last_func.params):
                if i < len(self.arg_registers):
                    self.emit(f"mov {self.arg_registers[i]}, {i+1}")
            self.emit(f"call {last_func.name}")
            self.emit("mov rsi, rax")
            self.emit("mov rdi, format")
            self.emit("xor rax, rax")
            self.emit("call printf")

        for instr in instructions:
            if not isinstance(instr, IRFunctionStart) or instr.name == "func_main":
                self.translate(instr)

        self.emit("call getchar")
        self.emit("mov rax, 60")
        self.emit("xor rdi, rdi")
        self.emit("syscall")

        return "\n".join(self.lines)

    def emit(self, line):
        self.lines.append(line)

    def emit_string_literals(self):
        for name, value in self.string_literals.items():
            self.emit(f'{name} db "{value}", 0')

    def extract_string_literals(self, instructions):
        for instr in instructions:
            for val in vars(instr).values():
                self._check_and_store_string(val)

    def _check_and_store_string(self, val):
        if isinstance(val, str) and val.startswith('"') and val.endswith('"'):
            value = val.strip('"')
            if value not in self.string_literals.values():
                name = f"str_{self.string_counter}"
                self.string_literals[name] = value
                self.string_counter += 1

    def collect_variables(self, instructions):
        seen = set()
        skip_prefixes = ("case_", "default_case", "end_match", "else_", "endif_", "while_", "for_", "try_", "catch_", "end_try")
        func_names = {instr.name for instr in instructions if isinstance(instr, IRFunctionStart)}
        for instr in instructions:
            for attr in vars(instr).values():
                if isinstance(attr, str) and attr.isidentifier():
                    if any(attr.startswith(p) for p in skip_prefixes) or attr in func_names:
                        continue
                    if attr not in seen:
                        self.emit(f"{attr} dq 0")
                        seen.add(attr)

    def resolve_value(self, val):
        if isinstance(val, str):
            if val.startswith('"') and val.endswith('"'):
                text = val.strip('"')
                for name, value in self.string_literals.items():
                    if value == text:
                        return f"[rel {name}]"
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

        elif isinstance(instr, IRFunctionEnd):
            self.emit("pop rbp")
            self.emit("ret")

        elif isinstance(instr, IRAssign):
            self.emit(f"mov rax, {self.resolve_value(instr.value)}")
            self.emit(f"mov qword [rel {instr.target}], rax")

        elif isinstance(instr, IRBinary):
            self.emit(f"mov rax, {self.resolve_value(instr.left)}")
            op = instr.op
            if op in {"+", "-", "*", "/"}:
                if op == "/":
                    self.emit("cqo")
                    self.emit(f"mov rbx, {self.resolve_value(instr.right)}")
                    self.emit("idiv rbx")
                else:
                    ops = {"+": "add", "-": "sub", "*": "imul"}
                    self.emit(f"{ops[op]} rax, {self.resolve_value(instr.right)}")
                self.emit(f"mov qword [rel {instr.result}], rax")
            elif op in {"==", "!=", "<", ">"}:
                cmps = {"==": "sete", "!=": "setne", "<": "setl", ">": "setg"}
                self.emit(f"cmp rax, {self.resolve_value(instr.right)}")
                self.emit(f"{cmps[op]} al")
                self.emit("movzx rax, al")
                self.emit(f"mov qword [rel {instr.result}], rax")
            elif op in {"&&", "||"}:
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
            if val.startswith("[rel str_"):
                self.emit("mov rdi, format_str")
                self.emit(f"lea rsi, {val}")
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
                cond = cond[1:]
                self.emit(f"mov rax, {self.resolve_value(cond)}")
                self.emit("cmp rax, 0")
                self.emit(f"je {instr.label}")
            else:
                self.emit(f"mov rax, {self.resolve_value(cond)}")
                self.emit("cmp rax, 0")
                self.emit(f"jne {instr.label}")

        elif isinstance(instr, IRLabel):
            if instr.label not in self.defined_labels:
                self.defined_labels.add(instr.label)
                self.emit(f"{instr.label}:")

        elif isinstance(instr, IRCall):
            for i, arg in enumerate(instr.args):
                val = self.resolve_value(arg)
                if i < len(self.arg_registers):
                    self.emit(f"mov {self.arg_registers[i]}, {val}")
                else:
                    self.emit(f"push {val}")
            self.emit(f"call {instr.name}")
            if len(instr.args) > len(self.arg_registers):
                self.emit(f"add rsp, {8 * (len(instr.args) - len(self.arg_registers))}")
            self.emit(f"mov qword [rel {instr.target}], rax")

        elif isinstance(instr, IRReturn):
            self.emit(f"mov rax, {self.resolve_value(instr.value)}")
            self.emit("pop rbp")
            self.emit("ret")

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
