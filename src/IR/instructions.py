class IRInstruction:
    pass


class IRAssign(IRInstruction):
    def __init__(self, target, value):
        self.target = target
        self.value = value
    def __repr__(self):
        return f"{self.target} = {self.value}"


class IRPrint(IRInstruction):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"print {self.value}"


class IRReturn(IRInstruction):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"return {self.value}"


class IRLabel(IRInstruction):
    def __init__(self, label):
        self.label = label
    def __repr__(self):
        return f"{self.label}:"


class IRGoto(IRInstruction):
    def __init__(self, label):
        self.label = label
    def __repr__(self):
        return f"goto {self.label}"


class IRIfGoto(IRInstruction):
    def __init__(self, condition, label):
        self.condition = condition
        self.label = label
    def __repr__(self):
        return f"if {self.condition} goto {self.label}"


class IRCall(IRInstruction):
    def __init__(self, target, name, args):
        self.target = target
        self.name = name
        self.args = args
    def __repr__(self):
        return f"{self.target} = call {self.name}({', '.join(self.args)})"


class IRBinary(IRInstruction):
    def __init__(self, result, left, op, right):
        self.result = result
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"{self.result} = {self.left} {self.op} {self.right}"


class IRUnary(IRInstruction):
    def __init__(self, result, op, operand):
        self.result = result
        self.op = op
        self.operand = operand
    def __repr__(self):
        return f"{self.result} = {self.op}{self.operand}"


class IRTryCatch(IRInstruction):
    def __init__(self, try_block, catch_block, exception_var):
        self.try_block = try_block
        self.catch_block = catch_block
        self.exception_var = exception_var
    def __repr__(self):
        return f"try {self.try_block} catch({self.exception_var}) {self.catch_block}"
