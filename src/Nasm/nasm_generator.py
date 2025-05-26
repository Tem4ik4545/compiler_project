from src.IR.instructions import *
from src.IR.temp_manager import TempManager
from src.AST.Karkas import MatchCase, DefaultCase

class NASMGenerator:
    def __init__(self):
        self.lines = []
        self.label_counter = 0
        self.win64_registers = ["rcx", "rdx", "r8", "r9"]
        self.string_literals = {}
        self.float_literals = {}  # Отдельный словарь для float-литералов
        self.string_counter = 0
        self.float_counter = 0    # Счётчик для float-литералов
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
        self.emit('format_float db "%.6f", 10, 0')
        self.emit('format_str db "%s", 10, 0')
        self.emit('div_zero_err db "Error: division by zero", 10, 0')
        if any(val.lower() == "true" for instr in instructions for val in vars(instr).values() if isinstance(val, str)):
            self.emit("True dq 1")
        if any(val.lower() == "false" for instr in instructions for val in vars(instr).values() if
               isinstance(val, str)):
            self.emit("False dq 0")
        self.collect_variables(instructions)
        self.extract_string_literals(instructions)
        self.emit_string_literals()
        self.emit_float_literals()

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

        self.emit("_float_div_zero:")
        self.emit("    sub rsp, 32")
        self.emit("    lea rcx, [rel div_zero_err]")
        self.emit("    xor rax, rax")
        self.emit("    call printf")
        self.emit("    call ExitProcess")

        self.emit("_int_div_zero:")
        self.emit("    sub rsp, 32")
        self.emit("    lea rcx, [rel div_zero_err]")
        self.emit("    xor rax, rax")
        self.emit("    call printf")
        self.emit("    call ExitProcess")
        return "\n".join(self.lines)

    def emit(self, line):
        self.lines.append(line)

    def emit_string_literals(self):
        for name, value in self.string_literals.items():
            self.emit(f'{name} db "{value}", 0')

    def emit_float_literals(self):
        for name, value in self.float_literals.items():
            self.emit("align 4")
            self.emit(f"{name} dd {value}")

    def _is_number_literal(self, var: str) -> bool:
        try:
            float(var)
            return True
        except ValueError:
            return False
    def _check_and_store_float(self, val):
        if isinstance(val, str) and '.' in val:
            if val not in self.float_literals.values():
                name = f"float_{self.float_counter}"
                self.float_literals[name] = val
                self.float_counter += 1

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
            for attr in ("value", "left", "right"):
                if hasattr(instr, attr):
                    val = getattr(instr, attr)
                    self._check_and_store_float(val)
            for attr in ("target", "result"):
                if hasattr(instr, attr):
                    val = getattr(instr, attr)
                    if isinstance(val, str):
                        var_type = getattr(instr, "type_", None)
                        self._add_variable(val, seen, func_names, var_type)
            for attr in ("left", "right", "value", "condition"):
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

    def _add_variable(self, var, seen, func_names, var_type_hint=None):
        if (var in seen
                or not isinstance(var, str)
                or var.isdigit()
                or self._is_number_literal(var)
                or var.startswith('"')
                or any(var.startswith(p) for p in self.skip_prefixes)
                or var in func_names
                or var.startswith("str_")
                or var in ("True", "False")):
            return

        var_type = var_type_hint or "int"
        for instr in self.ir_instructions:
            if isinstance(instr, IRAssign) and instr.target == var:
                var_type = instr.type_ or var_type
                break

        seen.add(var)
        self.defined_variables.add(var)

        if var_type == "float":
            self.emit("align 4")
            self.emit(f"{var} dd 0.0")  # 32-битный float
        else:
            self.emit(f"{var} dq 0")  # 64-битный int

    def resolve_value(self, val, type_=None):
        if isinstance(val, str):
            if '.' in val and (type_ == "float" or any(c.isalpha() for c in val)):
                for name, v in self.float_literals.items():
                    if v == val:
                        return f"[rel {name}]"
                return val
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

    def _get_var_type(self, var_name: str) -> str:
        """Возвращает тип переменной по её имени из IR-инструкций."""
        if isinstance(var_name, str):
            if var_name.startswith('"'):
                return "string"
            elif '.' in var_name and var_name.replace('.', '').replace('-', '').isdigit():
                return "float"
        for instr in self.ir_instructions:
            if hasattr(instr, "target") and getattr(instr, "target") == var_name:
                return getattr(instr, "type_", "int")
            if hasattr(instr, "result") and getattr(instr, "result") == var_name:
                return getattr(instr, "type_", "int")
        return "int"

    def translate(self, instr):
        if isinstance(instr, IRLabel):
            if instr.label not in self.defined_labels:
                self.defined_labels.add(instr.label)
                self.emit(f"{instr.label}:")
            return

        if isinstance(instr, IRAssign):
            if instr.type_ == "float":
                self.emit(f"    movss xmm0, {self.resolve_value(instr.value, 'float')}")
                self.emit(f"    movss [rel {instr.target}], xmm0")
            else:
                self.emit(f"    mov rax, {self.resolve_value(instr.value)}")
                self.emit(f"    mov [rel {instr.target}], rax")
            return

        if isinstance(instr, IRBinary):
            if instr.op in ("&&", "||"):
                self.translate_logical(instr)
                return
            if instr.type_ == "float":
                self.emit(f"    movss xmm0, {self.resolve_value(instr.left, 'float')}")
                self.emit(f"    movss xmm1, {self.resolve_value(instr.right, 'float')}")
                if instr.op == '+':
                    self.emit("    addss xmm0, xmm1")
                elif instr.op == '-':
                    self.emit("    subss xmm0, xmm1")
                elif instr.op == '*':
                    self.emit("    mulss xmm0, xmm1")
                elif instr.op == '/':
                    self.emit("    movss xmm2, xmm1")
                    self.emit("    xorps xmm3, xmm3")
                    self.emit("    ucomiss xmm2, xmm3")
                    self.emit("    je _float_div_zero")
                    self.emit("    divss xmm0, xmm1")
                self.emit(f"    movss [rel {instr.result}], xmm0")
            else:
                self.emit(f"    mov rax, {self.resolve_value(instr.left)}")
                if instr.op == "/":
                    self.emit(f"    mov rbx, {self.resolve_value(instr.right)}")
                    self.emit("    cmp rbx, 0")
                    self.emit("    je _int_div_zero")
                    self.emit("    cqo")
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
            var_type = instr.type_ if hasattr(instr, 'type_') and instr.type_ else self._get_var_type(instr.value)
            val = self.resolve_value(instr.value, var_type)
            self.emit(f"    sub rsp, {self.shadow_space}")
            if var_type == "float":
                self.emit(f"    movss xmm0, {val}")
                self.emit("    cvtss2sd xmm0, xmm0")
                self.emit("    movq rdx, xmm0")
                self.emit("    mov rcx, format_float")
                self.emit("    mov rax, 1")
            elif var_type == "string":
                self.emit(f"    lea rdx, {val}")
                self.emit("    mov rcx, format_str")
                self.emit("    xor rax, rax")
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
