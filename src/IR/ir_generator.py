from src.IR.temp_manager import TempManager
from src.IR.instructions import *

class IRGenerator:
    def __init__(self):
        self.temp = TempManager()
        self.instructions = []

    def generate(self, node):
        self.visit(node)
        return self.instructions

    def visit(self, node):
        if isinstance(node, list):
            for item in node:
                self.visit(item)
            return

        method = f"visit_{type(node).__name__}"
        return getattr(self, method, self.generic_visit)(node)

    def generic_visit(self, node):
        raise Exception(f"No visit method for {type(node).__name__}")

    def visit_Program(self, node):
        for stmt in node.statements:
            if stmt is None:
                continue
            result = self.visit(stmt)
            if isinstance(result, list):
                self.instructions.extend(result)

    def visit_VarDeclaration(self, node):
        value = self.visit(node.value)
        self.instructions.append(IRAssign(node.name, value))

    def visit_Assignment(self, node):
        value = self.visit(node.value)
        self.instructions.append(IRAssign(node.name, value))

    def visit_PrintStatement(self, node):
        value = self.visit(node.expression)
        self.instructions.append(IRPrint(value))

    def visit_Return(self, node):
        value = self.visit(node.value)
        self.instructions.append(IRReturn(value))

    def visit_IfStatement(self, node):
        else_label = self.temp.new_label("else")
        end_label = self.temp.new_label("endif")

        condition = self.visit(node.condition)
        self.instructions.append(IRIfGoto(f"!{condition}", else_label))

        self.visit(node.then_block)
        self.instructions.append(IRGoto(end_label))

        self.instructions.append(IRLabel(else_label))
        if node.else_block:
            self.visit(node.else_block)
        self.instructions.append(IRLabel(end_label))

    def visit_WhileStatement(self, node):
        start_label = self.temp.new_label("while_start")
        end_label = self.temp.new_label("while_end")

        self.instructions.append(IRLabel(start_label))
        condition = self.visit(node.condition)
        self.instructions.append(IRIfGoto(f"!{condition}", end_label))

        self.visit(node.body)
        self.instructions.append(IRGoto(start_label))
        self.instructions.append(IRLabel(end_label))

    def visit_ForStatement(self, node):
        self.visit(node.init)
        start_label = self.temp.new_label("for_start")
        end_label = self.temp.new_label("for_end")

        self.instructions.append(IRLabel(start_label))
        condition = self.visit(node.condition)
        self.instructions.append(IRIfGoto(f"!{condition}", end_label))

        self.visit(node.body)
        self.visit(node.update)
        self.instructions.append(IRGoto(start_label))
        self.instructions.append(IRLabel(end_label))

    def visit_FunctionDeclaration(self, node):
        self.instructions.append(IRFunctionStart(f"func_{node.name}", [name for name, _ in node.params]))
        for stmt in node.body.statements:
            if stmt is not None:
                self.visit(stmt)
        self.instructions.append(IRFunctionEnd(f"func_{node.name}"))

    def visit_ReturnStatement(self, node):
        value = self.visit(node.value) if node.value else None
        self.instructions.append(IRReturn(value))


    def visit_FunctionCall(self, node):
        args = [self.visit(arg) for arg in node.arguments]
        result = self.temp.new_temp()
        self.instructions.append(IRCall(result, node.name, args))
        return result

    def visit_BinaryOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        result = self.temp.new_temp()
        self.instructions.append(IRBinary(result, left, node.op, right))
        return result

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        result = self.temp.new_temp()
        self.instructions.append(IRUnary(result, node.op, operand))
        return result

    def visit_Identifier(self, node):
        return node.name

    def visit_Literal(self, node):
        return str(node.value)

    def visit_Block(self, node):
        if not node.statements:
            return
        for stmt in node.statements:
            if stmt is None:
                continue
            if isinstance(stmt, list):
                for sub in stmt:
                    if sub is not None:
                        self.visit(sub)
            else:
                self.visit(stmt)

    def visit_TryCatchStatement(self, node):
        try_label = self.temp.new_label("try")
        catch_label = self.temp.new_label("catch")
        end_label = self.temp.new_label("end_try")

        self.instructions.append(IRLabel(try_label))
        self.visit(node.try_block)
        self.instructions.append(IRGoto(end_label))

        self.instructions.append(IRLabel(catch_label))
        self.visit(node.catch_block)

        self.instructions.append(IRLabel(end_label))

    def visit_MatchStatement(self, node):
        expr_temp = self.visit(node.expr)
        end_label = self.temp.new_label("end_match")
        case_labels = []

        for i, case in enumerate(node.cases):
            label = self.temp.new_label(f"case_{i}")
            case_labels.append((label, case))
            condition_temp = self.visit(case.value)
            cond = self.temp.new_temp()
            self.instructions.append(IRBinary(cond, expr_temp, "==", condition_temp))
            self.instructions.append(IRIfGoto(cond, label))

        if node.default:
            default_label = self.temp.new_label("default_case")
            self.instructions.append(IRGoto(default_label))
        else:
            self.instructions.append(IRGoto(end_label))

        for (label, case) in case_labels:
            self.instructions.append(IRLabel(label))
            for stmt in case.body:
                self.visit(stmt)
            self.instructions.append(IRGoto(end_label))

        if node.default:
            self.instructions.append(IRLabel(default_label))
            for stmt in node.default.body:
                self.visit(stmt)

        self.instructions.append(IRLabel(end_label))

