from src.IR.instructions import *


class IROptimizer:
    def optimize(self, instructions):
        instructions = self.constant_folding(instructions)
        instructions = self.copy_propagation(instructions)
        instructions = self.remove_unused_temps(instructions)
        instructions = self.remove_self_assignments(instructions)
        instructions = self.simplify_if_true(instructions)
        instructions = self.remove_dead_code_after_return(instructions)
        return instructions

    def constant_folding(self, instructions):
        result = []
        for instr in instructions:
            if isinstance(instr, IRBinary) \
               and isinstance(instr.left, (int, float)) \
               and isinstance(instr.right, (int, float)):
                if instr.op == "+":
                    v = instr.left + instr.right
                elif instr.op == "-":
                    v = instr.left - instr.right
                elif instr.op == "*":
                    v = instr.left * instr.right
                elif instr.op == "/":
                    v = instr.left / instr.right if instr.right != 0 else 0
                else:
                    result.append(instr)
                    continue
                # вместо IRBinary — подставляем прямую константу
                result.append(IRAssign(instr.result, v))
            else:
                result.append(instr)
        return result

    def copy_propagation(self, instructions):
        result = []
        env = {}

        def is_user_var(name):
            return isinstance(name, str) and not name.startswith("t") and not name.isdigit()

        for instr in instructions:
            # оставляем «как есть» границы функций и метки
            if isinstance(instr, (IRFunctionStart, IRFunctionEnd, IRLabel)):
                result.append(instr)
                continue

            if isinstance(instr, IRAssign):
                val = instr.value
                # если это пользовательская переменная и в env есть её замена — подставляем
                if is_user_var(val) and val in env:
                    val = env[val]
                result.append(IRAssign(instr.target, val))
                # запоминаем только подстановки между user-vars, не трогаем temps
                if is_user_var(instr.target) and is_user_var(instr.value):
                    env[instr.target] = val

            elif isinstance(instr, IRBinary):
                L, R = instr.left, instr.right
                if is_user_var(L) and L in env:
                    L = env[L]
                if is_user_var(R) and R in env:
                    R = env[R]
                result.append(IRBinary(L, R, instr.op, instr.result))

            elif isinstance(instr, IRPrint):
                v = instr.value
                if is_user_var(v) and v in env:
                    v = env[v]
                result.append(IRPrint(v))

            elif isinstance(instr, IRIfGoto):
                c = instr.condition
                if is_user_var(c) and c in env:
                    c = env[c]
                result.append(IRIfGoto(c, instr.label))

            elif isinstance(instr, IRCall):
                # полностью не трогаем имя функции и её целевой temp
                result.append(instr)

            else:
                result.append(instr)

        return result

    def remove_unused_temps(self, instructions):
        used = set()
        for instr in instructions:
            if isinstance(instr, IRPrint):
                used.add(instr.value)
            elif isinstance(instr, IRBinary):
                used.update([instr.left, instr.right, instr.result])
            elif isinstance(instr, IRReturn):
                used.add(instr.value)
            elif isinstance(instr, IRCall):
                if instr.target:
                    used.add(instr.target)
                used.update(instr.args)
            elif isinstance(instr, IRIfGoto):
                used.add(instr.condition)
            elif isinstance(instr, IRAssign) and isinstance(instr.value, str):
                used.add(instr.value)

        # удаляем только чисто временные присваивания, начинающиеся на "t"
        cleaned = []
        for instr in instructions:
            if isinstance(instr, IRAssign) \
               and isinstance(instr.target, str) \
               and instr.target.startswith("t") \
               and instr.target not in used:
                continue
            cleaned.append(instr)
        return cleaned

    def remove_self_assignments(self, instructions):
        return [
            instr for instr in instructions
            if not (isinstance(instr, IRAssign) and instr.target == instr.value)
        ]

    def simplify_if_true(self, instructions):
        result = []
        for instr in instructions:
            if isinstance(instr, IRIfGoto):
                if instr.condition == "true" or instr.condition is True:
                    result.append(IRGoto(instr.label))
                elif instr.condition == "false" or instr.condition is False:
                    # if false — просто удаляем
                    continue
                else:
                    result.append(instr)
            else:
                result.append(instr)
        return result

    def remove_dead_code_after_return(self, instructions):
        result = []
        skip = False
        for instr in instructions:
            # всегда сохраняем границы функций
            if isinstance(instr, (IRFunctionStart, IRFunctionEnd)):
                result.append(instr)
                skip = False
                continue
            if skip:
                # игнорим всё до конца функции
                continue
            result.append(instr)
            if isinstance(instr, IRReturn):
                skip = True
        return result
