from src.IR.instructions import *
from src.IR.temp_manager import TempManager
from src.AST.Karkas import MatchCase, DefaultCase

class NASMGenerator:
    def __init__(self):
        self.lines = []
        self.label_counter = 0
        self.win64_registers = ["rcx", "rdx", "r8", "r9"]
        self.string_literals = {}
        self.string_counter = 0
        self.defined_labels = set()
        self.defined_functions = set()
        self.shadow_space = 32
        self.defined_variables = set()
        self.ir_instructions = []
        self.skip_prefixes = (
            "case_", "default_case", "end_match", "else_", "endif_",
            "while_", "for_", "try_", "catch_", "end_try", "!"
        )

    def generate(self, instructions):
        self.lines.clear()
        self.string_literals.clear()
        self.defined_labels.clear()
        self.defined_functions.clear()
        self.string_counter = 0
        self.ir_instructions = instructions

        self.emit("section .data")
        self.emit("newline    db 10, 0")
        self.emit('format     db "%d", 10, 0')
        self.emit('format_str db "%s", 10, 0')
        if any(val.lower() == "true" for instr in instructions for val in vars(instr).values() if isinstance(val, str)):
            self.emit("True dq 1")
        if any(val.lower() == "false" for instr in instructions for val in vars(instr).values() if
               isinstance(val, str)):
            self.emit("False dq 0")
        self.collect_variables(instructions)
        self.extract_string_literals(instructions)
        self.emit_string_literals()

        self.emit("section .text")
        self.emit("default rel")
        self.emit("extern printf")
        self.emit("extern ExitProcess")
        self.emit("global main")

        i = 0
        while i < len(instructions):
            instr = instructions[i]
            if isinstance(instr, IRFunctionStart):
                self.emit(f"{instr.name}:")
                self.emit("    push rbp")
                self.emit("    mov rbp, rsp")
                i += 1
                while i < len(instructions) and not isinstance(instructions[i], IRFunctionEnd):
                    cur = instructions[i]
                    self.translate(cur)
                    i += 1
            i += 1

        self.emit("main:")
        self.emit(f"    sub rsp, {self.shadow_space}")
        inside_fn = False
        for instr in instructions:
            if isinstance(instr, IRFunctionStart):
                inside_fn = True
                continue
            if isinstance(instr, IRFunctionEnd):
                inside_fn = False
                continue
            if not inside_fn and not isinstance(instr, IRReturn):
                self.translate(instr)
        self.emit("    xor  ecx, ecx")
        self.emit("    call ExitProcess")
        self.emit(f"    add  rsp, {self.shadow_space}")
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
            text = val.strip('"')
            if text not in self.string_literals.values():
                name = f"str_{self.string_counter}"
                self.string_literals[name] = text
                self.string_counter += 1

    def collect_variables(self, instructions):
        seen = set()
        func_names = {instr.name for instr in instructions if isinstance(instr, IRFunctionStart)}
        for instr in instructions:
            for attr in ("target", "result", "left", "right", "value", "condition"):
                if hasattr(instr, attr):
                    val = getattr(instr, attr)
                    if isinstance(val, str):
                        self._add_variable(val, seen, func_names)
            if isinstance(instr, IRFunctionStart):
                for param in instr.params:
                    self._add_variable(param, seen, func_names)
            if isinstance(instr, IRCall):
                for arg in instr.args:
                    if isinstance(arg, str):
                        self._add_variable(arg, seen, func_names)

    def _add_variable(self, var, seen, func_names):
        if (not var or not isinstance(var, str)
                or var.isdigit()
                or var.startswith('"') and var.endswith('"')
                or any(var.startswith(p) for p in self.skip_prefixes)
                or var in func_names
                or var.startswith("str_")
                or var in ("True", "False")):  # <== добавлено
            return
        if var in seen:
            return
        seen.add(var)
        self.defined_variables.add(var)
        self.emit(f"{var} dq 0")

    def resolve_value(self, val):
        if isinstance(val, str):
            if val.startswith('"'):
                txt = val.strip('"')
                for name, v in self.string_literals.items():
                    if v == txt:
                        return f"[rel {name}]"
            val_lower = val.lower()
            if val in self.defined_variables:
                return f"[rel {val}]"
            if val_lower == "true":
                return "[rel True]"
            if val_lower == "false":
                return "[rel False]"
            if val.isnumeric():
                return val
        return str(val)

    def fresh_label(self, prefix):
        lbl = f"{prefix}_{self.label_counter}"
        self.label_counter += 1
        return lbl

    def get_function_params(self, func_name):
        # Простой способ найти параметры из IRFunctionStart
        for instr in self.ir_instructions:
            if isinstance(instr, IRFunctionStart) and instr.name == func_name:
                return instr.params
        return []

    def translate(self, instr):
        if isinstance(instr, IRLabel):
            if instr.label not in self.defined_labels:
                self.defined_labels.add(instr.label)
                self.emit(f"{instr.label}:")
            return

        if isinstance(instr, IRAssign):
            self.emit(f"    mov rax, {self.resolve_value(instr.value)}")
            self.emit(f"    mov [rel {instr.target}], rax")
            return

        if isinstance(instr, IRBinary):
            if instr.op in ("&&", "||"):
                self.translate_logical(instr)
                return
            self.emit(f"    mov rax, {self.resolve_value(instr.left)}")
            if instr.op == "/":
                self.emit("    cqo")
                self.emit(f"    mov rbx, {self.resolve_value(instr.right)}")
                self.emit("    idiv rbx")
            elif instr.op in {"+", "-", "*"}:
                op_map = {"+": "add", "-": "sub", "*": "imul"}
                self.emit(f"    {op_map[instr.op]} rax, {self.resolve_value(instr.right)}")
            else:
                cmp_map = {"==": "sete", "!=": "setne", "<": "setl", ">": "setg"}
                self.emit(f"    cmp rax, {self.resolve_value(instr.right)}")
                self.emit(f"    {cmp_map[instr.op]} al")
                self.emit("    movzx rax, al")
            self.emit(f"    mov [rel {instr.result}], rax")
            return

        if isinstance(instr, IRUnary):
            if instr.op == "!":
                self.emit(f"    mov rax, {self.resolve_value(instr.operand)}")
                self.emit("    cmp rax, 0")
                self.emit("    sete al")
                self.emit("    movzx rax, al")
                self.emit(f"    mov [rel {instr.result}], rax")
            return

        if isinstance(instr, IRPrint):
            val = self.resolve_value(instr.value)
            self.emit(f"    sub rsp, {self.shadow_space}")
            if val.startswith("[rel str_"):
                self.emit(f"    lea rdx, {val}")
                self.emit("    mov rcx, format_str")
            else:
                self.emit(f"    mov rdx, {val}")
                self.emit("    mov rcx, format")
            self.emit("    xor rax, rax")
            self.emit("    call printf")
            self.emit(f"    add rsp, {self.shadow_space}")
            return

        if isinstance(instr, IRGoto):
            self.emit(f"    jmp {instr.label}")
            return

        if isinstance(instr, IRIfGoto):
            cond = instr.condition
            if isinstance(cond, str) and cond.startswith("!"):
                var = cond[1:]
                self.emit(f"    mov rax, [rel {var}]")
                self.emit("    test rax, rax")
                self.emit(f"    je  {instr.label}")
            else:
                self.emit(f"    mov rax, [rel {cond}]")
                self.emit("    test rax, rax")
                self.emit(f"    jne {instr.label}")
            return

        if isinstance(instr, IRCall):
            # 1. Передаём аргументы в регистры или стек
            for i, arg in enumerate(instr.args):
                val = self.resolve_value(arg)
                if i < len(self.win64_registers):
                    reg = self.win64_registers[i]
                    self.emit(f"    mov {reg}, {val}")
                else:
                    offset = 32 + (i - 4) * 8
                    self.emit(f"    mov qword [rsp + {offset}], {val}")

            # 2. Явно записываем параметры в переменные перед вызовом
            func_name = instr.name
            param_names = self.get_function_params(func_name)

            for i, param in enumerate(param_names):
                if i < len(self.win64_registers):
                    reg = self.win64_registers[i]
                    self.emit(f"    mov [rel {param}], {reg}")
                else:
                    offset = 32 + (i - 4) * 8
                    self.emit(f"    mov rax, qword [rsp + {offset}]")
                    self.emit(f"    mov [rel {param}], rax")

            # 3. Вызов функции и сохранение результата
            sp = max(32, 8 * len(instr.args)) & ~15
            self.emit(f"    sub rsp, {sp}")
            self.emit(f"    call {instr.name}")
            self.emit(f"    add rsp, {sp}")
            if instr.target:
                self.emit(f"    mov [rel {instr.target}], rax")
            return

        if isinstance(instr, IRReturn):
            if instr.value is not None:
                self.emit(f"    mov rax, {self.resolve_value(instr.value)}")
            self.emit("    mov rsp, rbp")
            self.emit("    pop rbp")
            self.emit("    ret")
            return

        if isinstance(instr, MatchCase):
            self.emit(f"{instr.label}:")
            for s in instr.body:
                self.translate(s)
            self.emit(f"    jmp {instr.end_label}")
            return

        if isinstance(instr, DefaultCase):
            self.emit(f"{instr.label}:")
            for s in instr.body:
                self.translate(s)
            self.emit(f"{instr.end_label}:")
            return

    def translate_logical(self, instr):
        skip = self.fresh_label("skip")
        end = self.fresh_label("end")
        self.emit(f"    mov rax, {self.resolve_value(instr.left)}")
        self.emit("    cmp rax, 0")
        self.emit(f"    {'je' if instr.op == '&&' else 'jne'} {skip}")
        self.emit(f"    mov rax, {self.resolve_value(instr.right)}")
        self.emit("    cmp rax, 0")
        self.emit("    setne al")
        self.emit(f"    jmp {end}")
        self.emit(f"{skip}:")
        self.emit(f"    mov al, {'0' if instr.op == '&&' else '1'}")
        self.emit(f"{end}:")
        self.emit("    movzx rax, al")
        self.emit(f"    mov [rel {instr.result}], rax")
