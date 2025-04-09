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
                if instr.op == "+":
                    value = instr.left + instr.right
                elif instr.op == "-":
                    value = instr.left - instr.right
                elif instr.op == "*":
                    value = instr.left * instr.right
                elif instr.op == "/":
                    value = instr.left / instr.right if instr.right != 0 else 0
                else:
                    result.append(instr)
                    continue
                result.append(IRAssign(instr.result, value))
            else:
                result.append(instr)
        return result

    def copy_propagation(self, instructions):
        result = []
        env = {}
        for instr in instructions:
            if isinstance(instr, IRAssign) and isinstance(instr.value, str):
                env[instr.target] = env.get(instr.value, instr.value)
                result.append(IRAssign(instr.target, env[instr.target]))
            elif isinstance(instr, IRPrint):
                value = env.get(instr.value, instr.value)
                result.append(IRPrint(value))
            else:
                result.append(instr)
        return result

    def remove_unused_temps(self, instructions):
        used = set()
        for instr in instructions:
            if isinstance(instr, IRPrint):
                used.add(instr.value)
            elif isinstance(instr, IRBinary):
                used.update([instr.left, instr.right])
            elif isinstance(instr, IRReturn):
                used.add(instr.value)

        return [instr for instr in instructions
                if not (isinstance(instr, IRAssign) and instr.target not in used)]

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
                else:
                    result.append(instr)
            else:
                result.append(instr)
        return result

    def remove_dead_code_after_return(self, instructions):
        result = []
        skip = False
        for instr in instructions:
            if skip and not isinstance(instr, IRLabel):
                continue
            result.append(instr)
            if isinstance(instr, IRReturn):
                skip = True
            elif isinstance(instr, IRLabel):
                skip = False
        return result
