class IRInstruction:
    pass


class IRAssign(IRInstruction):
    def __init__(self, target, value, type_=None):
        self.target = target
        self.value = value
        self.type_ = type_
    def __repr__(self):
        type_str = f" (type={self.type_})" if self.type_ else ""
        return f"{self.target} = {self.value}{type_str}"


class IRPrint(IRInstruction):
    def __init__(self, value, type_=None):
        self.value = value
        self.type_ = type_
    def __repr__(self):
        type_str = f" (type={self.type_})" if self.type_ else ""
        return f"print {self.value}{type_str}"


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
        args_str = ', '.join(map(str, self.args))
        return f"{self.target} = call {self.name}({args_str})"


class IRFunctionStart:
    def __init__(self, name, params=None):
        self.name = name
        self.params = params or []

    def __str__(self):
        return f"{self.name}:\nparams: {', '.join(self.params)}"

class IRFunctionEnd:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"; end {self.name}"


class IRBinary(IRInstruction):
    def __init__(self, result, left, op, right, type_=None):
        self.result = result
        self.left = left
        self.op = op
        self.right = right
        self.type_ = type_
    def __repr__(self):
        type_str = f" (type={self.type_})" if self.type_ else ""
        return f"{self.result} = {self.left} {self.op} {self.right}{type_str}"


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
