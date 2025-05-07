from src.IR.instructions import *
from src.IR.temp_manager import TempManager
from src.AST.Karkas import MatchCase, DefaultCase

class NASMGenerator:
    def __init__(self):
        self.lines = []
        self.label_counter = 0
        self.win64_registers = ["rcx", "rdx", "r8", "r9"]
        self.func_params = {}
        self.string_literals = {}
        self.string_counter = 0
        self.defined_labels = set()
        self.defined_functions = set()
        self.shadow_space = 32
        self.defined_variables = set()

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
        self.emit("default rel")
        self.emit("extern printf")
        self.emit("extern ExitProcess")
        self.emit("global main")

        for instr in instructions:
            if isinstance(instr, IRFunctionStart):
                self.translate(instr)

        self.emit("main:")
        self.emit("sub rsp, 40")

        for instr in instructions:
            if not isinstance(instr, IRFunctionStart):
                self.translate(instr)

        self.emit("xor ecx, ecx")
        self.emit("call ExitProcess")
        self.emit("add rsp, 40")
        return "\n".join(self.lines)

    def emit(self, line):
        self.lines.append(line)

    def emit_string_literals(self):
        for name, value in self.string_literals.items():
            self.emit(f'{name} db "{value}", 10, 0')

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
        skip_prefixes = (
        "case_", "default_case", "end_match", "else_", "endif_", "while_", "for_", "try_", "catch_", "end_try")
        func_names = {instr.name for instr in instructions if isinstance(instr, IRFunctionStart)}

        for instr in instructions:
            if isinstance(instr, IRFunctionStart):
                for param in instr.params:
                    if param not in seen and param not in func_names:
                        self.emit(f"{param} dq 0")
                        seen.add(param)
                        self.defined_variables.add(param)

        for instr in instructions:
            if isinstance(instr, IRAssign):
                self._add_variable(instr.target, seen, skip_prefixes, func_names)
            if hasattr(instr, "result"):
                self._add_variable(instr.result, seen, skip_prefixes, func_names)

    def _add_variable(self, var_name, seen, skip_prefixes, func_names):
        if (var_name and
                var_name not in seen and
                not any(var_name.startswith(p) for p in skip_prefixes) and
                var_name not in func_names and
                not var_name.startswith("str_")):
            self.emit(f"{var_name} dq 0")
            seen.add(var_name)
            self.defined_variables.add(var_name)

    def resolve_value(self, val):
        if isinstance(val, str):
            if val.startswith('"'):
                text = val.strip('"')
                for name, value in self.string_literals.items():
                    if value == text:
                        return f"[rel {name}]"
            elif val in self.defined_variables:
                return f"[rel {val}]"
            elif val == "True":
                return "[rel True]"
            elif val == "False":
                return "[rel False]"
            elif val.isnumeric():
                return val
        return str(val)

    def translate(self, instr):

        if isinstance(instr, IRFunctionStart):
            if instr.name in self.defined_functions:
                return
            self.defined_functions.add(instr.name)
            self.emit(f"{instr.name}:")
            self.emit("push rbp")
            self.emit("mov rbp, rsp")
            for i, param in enumerate(instr.params):
                if i < 4:
                    reg = self.win64_registers[i]
                    self.emit(f"mov [rel {param}], {reg}")
                else:
                    offset = 8 * (i - 4) + 32
                    self.emit(f"mov rax, [rbp + {offset}]")
                    self.emit(f"mov [rel {param}], rax")

        elif isinstance(instr, IRFunctionEnd):
            self.emit("pop rbp")
            self.emit("ret")

        elif isinstance(instr, IRAssign):
            self.emit(f"mov rax, {self.resolve_value(instr.value)}")
            self.emit(f"mov qword [rel {instr.target}], rax")

        elif isinstance(instr, IRBinary):
            self.emit(f"mov rax, {self.resolve_value(instr.left)}")
            if instr.op == "/":
                self.emit("cqo")
                self.emit(f"mov rbx, {self.resolve_value(instr.right)}")
                self.emit("idiv rbx")
            elif instr.op in {"+", "-", "*"}:
                ops = {"+": "add", "-": "sub", "*": "imul"}
                self.emit(f"{ops[instr.op]} rax, {self.resolve_value(instr.right)}")
            elif instr.op in {"==", "!=", "<", ">"}:
                cmps = {"==": "sete", "!=": "setne", "<": "setl", ">": "setg"}
                self.emit(f"cmp rax, {self.resolve_value(instr.right)}")
                self.emit(f"{cmps[instr.op]} al")
                self.emit("movzx rax, al")
            self.emit(f"mov qword [rel {instr.result}], rax")

        elif isinstance(instr, IRUnary) and instr.op == "!":
            self.emit(f"mov rax, {self.resolve_value(instr.operand)}")
            self.emit("cmp rax, 0")
            self.emit("sete al")
            self.emit("movzx rax, al")
            self.emit(f"mov qword [rel {instr.result}], rax")


        elif isinstance(instr, IRPrint):
            val = self.resolve_value(instr.value)
            self.emit("sub rsp, 40")
            if val.startswith("[rel str_"):
                self.emit(f"lea rdx, {val}")
                self.emit("mov rcx, format_str")
            else:
                if val.isdigit():
                    self.emit(f"mov rdx, {val}")
                else:
                    self.emit(f"mov rdx, {val}")
                self.emit("mov rcx, format")
            self.emit("xor rax, rax")
            self.emit("call printf")
            self.emit("add rsp, 40")

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
                resolved = self.resolve_value(arg)
                if i < 4:
                    self.emit(f"mov {self.win64_registers[i]}, {resolved}")
                else:
                    offset = 32 + (i - 4) * 8
                    self.emit(f"mov [rsp + {offset}], {resolved}")
            stack_space = max(32, 8 * len(instr.args))
            stack_space = (stack_space + 15) & ~15
            self.emit(f"sub rsp, {stack_space}")
            self.emit(f"call {instr.name}")
            self.emit(f"add rsp, {stack_space}")
            if instr.target:
                self.emit(f"mov [rel {instr.target}], rax")


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
        self.emit("setne al" if instr.op == "||" else "sete al")
        self.emit("movzx rbx, al")
        self.emit(f"mov rax, {self.resolve_value(instr.right)}")
        self.emit("cmp rax, 0")
        self.emit("setne al" if instr.op == "||" else "sete al")
        self.emit("movzx rax, al")
        self.emit("or rax, rbx" if instr.op == "||" else "and rax, rbx")
        self.emit(f"mov qword [rel {instr.result}], rax")
