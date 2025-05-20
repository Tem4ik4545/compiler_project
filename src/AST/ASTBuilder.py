from src.parser.MyLangParser import MyLangParser
from src.AST.MyLangVisitor import MyLangVisitor
from src.AST.Karkas import *


class ASTBuilder(MyLangVisitor):
    def visitProgram(self, ctx: MyLangParser.ProgramContext):
        statements = []
        for stmt_ctx in ctx.statement():
            stmt = self.visit(stmt_ctx)
            if stmt is None:
                continue
            if isinstance(stmt, list):
                statements.extend(stmt)
            else:
                statements.append(stmt)
        return Program(statements=statements)

    def visitVarDeclaration(self, ctx: MyLangParser.VarDeclarationContext):
        name = ctx.ID().getText()
        type_ = ctx.type_().getText()
        value = self.visit(ctx.expression())
        return VarDeclaration(name, type_, value)

    def visitAssignment(self, ctx: MyLangParser.AssignmentContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return Assignment(name, value)

    def visitPrintStatement(self, ctx: MyLangParser.PrintStatementContext):
        expr = self.visit(ctx.expression())
        return PrintStatement(expr)

    def visitReturnStatement(self, ctx: MyLangParser.ReturnStatementContext):
        return ReturnStatement(self.visit(ctx.expression()) if ctx.expression() else None)

    def visitIfStatement(self, ctx: MyLangParser.IfStatementContext):
        cond = self.visit(ctx.expression())
        then_block = self.visit(ctx.block(0))
        else_block = self.visit(ctx.block(1)) if ctx.ELSE() else None
        return IfStatement(cond, then_block, else_block)

    def visitWhileStatement(self, ctx: MyLangParser.WhileStatementContext):
        cond = self.visit(ctx.expression())
        body = self.visit(ctx.block())
        return WhileStatement(cond, body)

    def visitForStatement(self, ctx: MyLangParser.ForStatementContext):
        init = self.visit(ctx.forInit()) if ctx.forInit() else None
        cond = self.visit(ctx.forCondition()) if ctx.forCondition() else None
        update = self.visit(ctx.forUpdate()) if ctx.forUpdate() else None
        body = self.visit(ctx.block())
        return ForStatement(init, cond, update, body)

    def visitForInit(self, ctx: MyLangParser.ForInitContext):
        return self.visit(ctx.getChild(0))

    def visitForCondition(self, ctx: MyLangParser.ForConditionContext):
        return self.visit(ctx.expression())

    def visitForUpdate(self, ctx: MyLangParser.ForUpdateContext):
        return self.visit(ctx.assignmentWithoutSemi())

    def visitVarDeclarationWithoutSemi(self, ctx: MyLangParser.VarDeclarationWithoutSemiContext):
        name = ctx.ID().getText()
        type_ = ctx.type_().getText()
        value = self.visit(ctx.expression())
        return VarDeclaration(name, type_, value)

    def visitAssignmentWithoutSemi(self, ctx: MyLangParser.AssignmentWithoutSemiContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        return Assignment(name, value)

    def visitBlock(self, ctx: MyLangParser.BlockContext):
        statements = []
        for stmt in ctx.statement():
            result = self.visit(stmt)
            if result is None:
                continue
            if isinstance(result, list):
                statements.extend(result)
            else:
                statements.append(result)
        return Block(statements)

    def visitTryCatchStatement(self, ctx: MyLangParser.TryCatchStatementContext):
        try_block = self.visit(ctx.block(0))
        catch_block = self.visit(ctx.block(1))
        if isinstance(try_block, list):
            try_block = Block(try_block)
        if isinstance(catch_block, list):
            catch_block = Block(catch_block)
        return TryCatchStatement(try_block, ctx.ID().getText(), catch_block)

    def visitMatchStatement(self, ctx: MyLangParser.MatchStatementContext):
        expr = self.visit(ctx.expression())
        cases = [self.visit(case) for case in ctx.matchCase()]
        default = self.visit(ctx.defaultCase()) if ctx.defaultCase() else None
        return MatchStatement(expr, cases, default)

    def visitMatchCase(self, ctx: MyLangParser.MatchCaseContext):
        value = self.visit(ctx.expression())
        statements = []
        for s in ctx.statement():
            res = self.visit(s)
            if res is None:
                continue
            if isinstance(res, list):
                statements.extend(res)
            else:
                statements.append(res)
        return MatchCase(value, statements)

    def visitDefaultCase(self, ctx: MyLangParser.DefaultCaseContext):
        statements = []
        for s in ctx.statement():
            res = self.visit(s)
            if res is None:
                continue
            if isinstance(res, list):
                statements.extend(res)
            else:
                statements.append(res)
        return DefaultCase(statements)

    def visitFunctionDeclaration(self, ctx: MyLangParser.FunctionDeclarationContext):
        name = ctx.ID().getText()
        params = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                params.append((p.ID().getText(), p.type_().getText()))
        return_type = ctx.type_().getText()
        body = self.visit(ctx.block())
        if isinstance(body, list):
            body = Block(body)
        return FunctionDeclaration(name, params, return_type, body)

    def visitExprFunctionCall(self, ctx: MyLangParser.ExprFunctionCallContext):
        name = ctx.ID().getText()
        args = [self.visit(e) for e in ctx.argList().expression()] if ctx.argList() else []
        return FunctionCall(name, args)

    def visitExprNot(self, ctx: MyLangParser.ExprNotContext):
        operand = self.visit(ctx.expression())
        if isinstance(operand, list):
            operand = operand[0]
        return UnaryOp("!", operand)

    def visitExprMulDiv(self, ctx: MyLangParser.ExprMulDivContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if isinstance(left, list):
            left = left[0]
        if isinstance(right, list):
            right = right[0]
        return BinaryOp(left, ctx.getChild(1).getText(), right)

    def visitExprAddSub(self, ctx: MyLangParser.ExprAddSubContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if isinstance(left, list):
            left = left[0]
        if isinstance(right, list):
            right = right[0]
        return BinaryOp(left, ctx.getChild(1).getText(), right)

    def visitExprComparison(self, ctx: MyLangParser.ExprComparisonContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if isinstance(left, list):
            left = left[0]
        if isinstance(right, list):
            right = right[0]
        return BinaryOp(left, ctx.getChild(1).getText(), right)

    def visitExprLogicalAnd(self, ctx: MyLangParser.ExprLogicalAndContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return BinaryOp(left, '&&', right)

    def visitExprLogicalOr(self, ctx: MyLangParser.ExprLogicalOrContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return BinaryOp(left, '||', right)

    def visitExprIdentifier(self, ctx: MyLangParser.ExprIdentifierContext):
        name = ctx.ID().getText()
        if name == "true":
            return Literal(True)
        if name == "false":
            return Literal(False)
        return Identifier(name)

    def visitExprPrimary(self, ctx: MyLangParser.ExprPrimaryContext):
        return self.visit(ctx.primary())

    def visitPrimary(self, ctx: MyLangParser.PrimaryContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        return self.visit(ctx.expression())

    def visitLiteral(self, ctx: MyLangParser.LiteralContext):
        text = ctx.getText()
        if ctx.INT_LITERAL():
            return Literal(int(text))
        if ctx.FLOAT_LITERAL():
            return Literal(float(text))
        if ctx.STRING_LITERAL():
            return Literal(text.strip('"'))
        if ctx.BOOL_LITERAL():
            return Literal(text == "true")

    def visitChildren(self, node):
        results = []
        for i in range(node.getChildCount()):
            child = self.visit(node.getChild(i))
            if child is not None:
                if isinstance(child, list):
                    results.extend(child)
                else:
                    results.append(child)
        return results
