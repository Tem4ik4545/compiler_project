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
            if isinstance(instr, IRBinary) and isinstance(instr.left, (int, float)) and isinstance(instr.right, (int, float)):
                try:
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
                    result.append(IRAssign(instr.result, v))
                except Exception:
                    result.append(instr)
            else:
                result.append(instr)
        return result

    def copy_propagation(self, instructions):
        result = []
        env = {}

        def is_temp(n):
            return isinstance(n, str) and n.startswith("t")

        for instr in instructions:

            if isinstance(instr, (IRFunctionStart, IRFunctionEnd, IRLabel)):
                result.append(instr)
                env.clear()
                continue

            if isinstance(instr, IRAssign) \
                    and is_temp(instr.target) \
                    and isinstance(instr.value, str) \
                    and is_temp(instr.value):
                src = instr.value
                final = env.get(src, src)
                result.append(IRAssign(instr.target, final))

                env.pop(instr.target, None)
                env[instr.target] = final
            else:
                result.append(instr)
                if isinstance(instr, (IRBinary, IRAssign, IRCall)) and hasattr(instr, 'result') and is_temp(
                        instr.result):
                    env.pop(instr.result, None)
                if isinstance(instr, IRAssign) and is_temp(instr.target):
                    env.pop(instr.target, None)
                if isinstance(instr, IRCall) and instr.target is not None and is_temp(instr.target):
                    env.pop(instr.target, None)
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

        cleaned = []
        for instr in instructions:
            if isinstance(instr, IRAssign) and isinstance(instr.target, str) and instr.target.startswith("t") and instr.target not in used:
                continue
            cleaned.append(instr)
        return cleaned

    def remove_self_assignments(self, instructions):
        return [instr for instr in instructions if not (isinstance(instr, IRAssign) and instr.target == instr.value)]

    def simplify_if_true(self, instructions):
        result = []
        for instr in instructions:
            if isinstance(instr, IRIfGoto):
                if instr.condition == "true" or instr.condition is True:
                    result.append(IRGoto(instr.label))
                elif instr.condition == "false" or instr.condition is False:
                    continue
                elif isinstance(instr.condition, str) and instr.condition.startswith("t"):

                    prev = result[-1] if result else None
                    if isinstance(prev, IRAssign) and prev.target == instr.condition:
                        if prev.value == "!True":
                            continue
                        if prev.value == "!False":
                            result.append(IRGoto(instr.label))
                        else:
                            result.append(instr)
                    else:
                        result.append(instr)
                else:
                    result.append(instr)
            else:
                result.append(instr)
        return result

    def remove_dead_code_after_return(self, instructions):
        result = []
        skip = False
        for instr in instructions:
            if isinstance(instr, (IRFunctionStart, IRFunctionEnd)):
                result.append(instr)
                skip = False
                continue
            if skip:
                continue
            result.append(instr)
            if isinstance(instr, IRReturn):
                skip = True
        return result
