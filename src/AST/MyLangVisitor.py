# Generated from src/parser/MyLang.g4 by ANTLR 4.13.2
from antlr4 import *

from src.parser.MyLangParser import MyLangParser


# This class defines a complete generic visitor for a parse tree produced by MyLangParser.

class MyLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLangParser#program.
    def visitProgram(self, ctx:MyLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#statement.
    def visitStatement(self, ctx:MyLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MyLangParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#assignment.
    def visitAssignment(self, ctx:MyLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MyLangParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#returnStatement.
    def visitReturnStatement(self, ctx:MyLangParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ifStatement.
    def visitIfStatement(self, ctx:MyLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#whileStatement.
    def visitWhileStatement(self, ctx:MyLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#forStatement.
    def visitForStatement(self, ctx:MyLangParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#forInit.
    def visitForInit(self, ctx:MyLangParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#forCondition.
    def visitForCondition(self, ctx:MyLangParser.ForConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#forUpdate.
    def visitForUpdate(self, ctx:MyLangParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#varDeclarationWithoutSemi.
    def visitVarDeclarationWithoutSemi(self, ctx:MyLangParser.VarDeclarationWithoutSemiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#assignmentWithoutSemi.
    def visitAssignmentWithoutSemi(self, ctx:MyLangParser.AssignmentWithoutSemiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#tryCatchStatement.
    def visitTryCatchStatement(self, ctx:MyLangParser.TryCatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#matchStatement.
    def visitMatchStatement(self, ctx:MyLangParser.MatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#matchCase.
    def visitMatchCase(self, ctx:MyLangParser.MatchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#defaultCase.
    def visitDefaultCase(self, ctx:MyLangParser.DefaultCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MyLangParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#paramList.
    def visitParamList(self, ctx:MyLangParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#param.
    def visitParam(self, ctx:MyLangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#block.
    def visitBlock(self, ctx:MyLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#printStatement.
    def visitPrintStatement(self, ctx:MyLangParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#argList.
    def visitArgList(self, ctx:MyLangParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprPrimary.
    def visitExprPrimary(self, ctx:MyLangParser.ExprPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprAddSub.
    def visitExprAddSub(self, ctx:MyLangParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprComparison.
    def visitExprComparison(self, ctx:MyLangParser.ExprComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprIdentifier.
    def visitExprIdentifier(self, ctx:MyLangParser.ExprIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprFunctionCall.
    def visitExprFunctionCall(self, ctx:MyLangParser.ExprFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprLogical.
    def visitExprLogical(self, ctx:MyLangParser.ExprLogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprMulDiv.
    def visitExprMulDiv(self, ctx:MyLangParser.ExprMulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#ExprNot.
    def visitExprNot(self, ctx:MyLangParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#primary.
    def visitPrimary(self, ctx:MyLangParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#binaryOp.
    def visitBinaryOp(self, ctx:MyLangParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#literal.
    def visitLiteral(self, ctx:MyLangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLangParser#type.
    def visitType(self, ctx:MyLangParser.TypeContext):
        return self.visitChildren(ctx)



del MyLangParser