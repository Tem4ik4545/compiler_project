

from typing import List, Optional, Union


class ASTNode:

    pass


class Program(ASTNode):
    def __init__(self, statements: List[ASTNode]):
        self.statements = statements

    def __repr__(self):
        return f"Program(statements={self.statements})"


class VarDeclaration(ASTNode):
    def __init__(self, name: str, type_: str, value: Optional[ASTNode]):
        self.name = name
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return f"VarDeclaration(name={self.name}, type_={self.type_}, value={self.value})"


class Assignment(ASTNode):
    def __init__(self, name: str, value: ASTNode):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Assignment(name={self.name}, value={self.value})"


class BinaryOp(ASTNode):
    def __init__(self, left: ASTNode, op: str, right: ASTNode):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinaryOp({self.left} {self.op} {self.right})"


class Literal(ASTNode):
    def __init__(self, value: Union[int, float, str, bool]):
        self.value = value

    def __repr__(self):
        return f"Literal(value={self.value})"


class Identifier(ASTNode):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Identifier(name={self.name})"


class PrintStatement(ASTNode):
    def __init__(self, expression: ASTNode):
        self.expression = expression

    def __repr__(self):
        return f"PrintStatement(expression={self.expression})"


class Block(ASTNode):
    def __init__(self, statements: List[ASTNode]):
        self.statements = statements

    def __repr__(self):
        return f"Block(statements={self.statements})"


class IfStatement(ASTNode):
    def __init__(self, condition: ASTNode, then_block: Block, else_block: Optional[Block] = None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def __repr__(self):
        return f"IfStatement(cond={self.condition}, then={self.then_block}, else={self.else_block})"


class WhileStatement(ASTNode):
    def __init__(self, condition: ASTNode, body: Block):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"WhileStatement(cond={self.condition}, body={self.body})"


class ForStatement(ASTNode):
    def __init__(self, init: Optional[ASTNode], condition: Optional[ASTNode],
                 update: Optional[ASTNode], body: Block):
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body

    def __repr__(self):
        return f"ForStatement(init={self.init}, cond={self.condition}, upd={self.update}, body={self.body})"


class FunctionDeclaration(ASTNode):
    def __init__(self, name: str, params: List[tuple], return_type: str, body: Block):
        self.name = name
        self.params = params  # список кортежей (имя, тип)
        self.return_type = return_type
        self.body = body

    def __repr__(self):
        return f"FunctionDeclaration(name={self.name}, params={self.params}, return_type={self.return_type}, body={self.body})"


class FunctionCall(ASTNode):
    def __init__(self, name: str, arguments: List[ASTNode]):
        self.name = name
        self.arguments = arguments

    def __repr__(self):
        return f"FunctionCall(name={self.name}, args={self.arguments})"


class TryCatchStatement(ASTNode):
    def __init__(self, try_block: Block, exception_name: str, catch_block: Block):
        self.try_block = try_block
        self.exception_name = exception_name
        self.catch_block = catch_block

    def __repr__(self):
        return f"TryCatch(try={self.try_block}, catch={self.catch_block})"


class MatchStatement(ASTNode):
    def __init__(self, expr: ASTNode, cases: List["MatchCase"], default: Optional[Block]):
        self.expr = expr
        self.cases = cases
        self.default = default

    def __repr__(self):
        return f"MatchStatement(expr={self.expr}, cases={self.cases}, default={self.default})"


class MatchCase(ASTNode):
    def __init__(self, value: ASTNode, body: List[ASTNode]):
        self.value = value
        self.body = body

    def __repr__(self):
        return f"MatchCase(value={self.value}, body={self.body})"


class ReturnStatement(ASTNode):
    def __init__(self, value: Optional[ASTNode]):
        self.value = value

    def __repr__(self):
        return f"Return(value={self.value})"
class UnaryOp(ASTNode):
    """ Унарная операция, например -x или !x """
    def __init__(self, op: str, operand: ASTNode):
        self.op = op
        self.operand = operand

class DefaultCase(ASTNode):
    def __init__(self, body: List[ASTNode]):
        self.body = body

    def __repr__(self):
        return f"DefaultCase(body={self.body})"
