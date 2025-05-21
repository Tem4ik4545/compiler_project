# Generated from src/parser/MyLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,289,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,5,0,61,8,0,10,0,12,0,64,9,0,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,80,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,
        5,3,5,100,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,111,8,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,122,8,8,1,8,1,8,3,8,126,8,
        8,1,8,1,8,3,8,130,8,8,1,8,1,8,1,8,1,9,1,9,3,9,137,8,9,1,10,1,10,
        1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,5,15,
        166,8,15,10,15,12,15,169,9,15,1,15,3,15,172,8,15,1,15,1,15,1,16,
        1,16,1,16,1,16,5,16,180,8,16,10,16,12,16,183,9,16,1,16,1,16,3,16,
        187,8,16,1,17,1,17,1,17,5,17,192,8,17,10,17,12,17,195,9,17,1,18,
        1,18,1,18,1,18,3,18,201,8,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,
        1,19,5,19,211,8,19,10,19,12,19,214,9,19,1,20,1,20,1,20,1,20,1,21,
        1,21,5,21,222,8,21,10,21,12,21,225,9,21,1,21,1,21,1,22,1,22,1,22,
        1,22,1,22,1,22,1,23,1,23,1,23,5,23,238,8,23,10,23,12,23,241,9,23,
        1,24,1,24,1,24,1,24,1,24,1,24,3,24,249,8,24,1,24,1,24,1,24,3,24,
        254,8,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,5,24,271,8,24,10,24,12,24,274,9,24,1,25,1,25,
        1,25,1,25,1,25,3,25,281,8,25,1,26,1,26,1,27,1,27,1,28,1,28,1,28,
        0,1,48,29,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,0,6,1,0,13,14,1,0,11,12,2,0,1,2,15,18,
        1,0,11,20,1,0,42,45,1,0,36,40,295,0,58,1,0,0,0,2,79,1,0,0,0,4,81,
        1,0,0,0,6,89,1,0,0,0,8,94,1,0,0,0,10,97,1,0,0,0,12,103,1,0,0,0,14,
        112,1,0,0,0,16,118,1,0,0,0,18,136,1,0,0,0,20,138,1,0,0,0,22,140,
        1,0,0,0,24,142,1,0,0,0,26,149,1,0,0,0,28,153,1,0,0,0,30,161,1,0,
        0,0,32,175,1,0,0,0,34,188,1,0,0,0,36,196,1,0,0,0,38,207,1,0,0,0,
        40,215,1,0,0,0,42,219,1,0,0,0,44,228,1,0,0,0,46,234,1,0,0,0,48,253,
        1,0,0,0,50,280,1,0,0,0,52,282,1,0,0,0,54,284,1,0,0,0,56,286,1,0,
        0,0,58,62,5,3,0,0,59,61,3,2,1,0,60,59,1,0,0,0,61,64,1,0,0,0,62,60,
        1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,66,5,4,0,0,
        66,67,5,0,0,1,67,1,1,0,0,0,68,80,3,4,2,0,69,80,3,6,3,0,70,80,3,36,
        18,0,71,80,3,8,4,0,72,80,3,12,6,0,73,80,3,14,7,0,74,80,3,16,8,0,
        75,80,3,28,14,0,76,80,3,30,15,0,77,80,3,10,5,0,78,80,3,44,22,0,79,
        68,1,0,0,0,79,69,1,0,0,0,79,70,1,0,0,0,79,71,1,0,0,0,79,72,1,0,0,
        0,79,73,1,0,0,0,79,74,1,0,0,0,79,75,1,0,0,0,79,76,1,0,0,0,79,77,
        1,0,0,0,79,78,1,0,0,0,80,3,1,0,0,0,81,82,5,22,0,0,82,83,5,41,0,0,
        83,84,5,8,0,0,84,85,3,56,28,0,85,86,5,10,0,0,86,87,3,48,24,0,87,
        88,5,7,0,0,88,5,1,0,0,0,89,90,5,41,0,0,90,91,5,10,0,0,91,92,3,48,
        24,0,92,93,5,7,0,0,93,7,1,0,0,0,94,95,3,48,24,0,95,96,5,7,0,0,96,
        9,1,0,0,0,97,99,5,33,0,0,98,100,3,48,24,0,99,98,1,0,0,0,99,100,1,
        0,0,0,100,101,1,0,0,0,101,102,5,7,0,0,102,11,1,0,0,0,103,104,5,23,
        0,0,104,105,5,5,0,0,105,106,3,48,24,0,106,107,5,6,0,0,107,110,3,
        42,21,0,108,109,5,24,0,0,109,111,3,42,21,0,110,108,1,0,0,0,110,111,
        1,0,0,0,111,13,1,0,0,0,112,113,5,25,0,0,113,114,5,5,0,0,114,115,
        3,48,24,0,115,116,5,6,0,0,116,117,3,42,21,0,117,15,1,0,0,0,118,119,
        5,26,0,0,119,121,5,5,0,0,120,122,3,18,9,0,121,120,1,0,0,0,121,122,
        1,0,0,0,122,123,1,0,0,0,123,125,5,7,0,0,124,126,3,20,10,0,125,124,
        1,0,0,0,125,126,1,0,0,0,126,127,1,0,0,0,127,129,5,7,0,0,128,130,
        3,22,11,0,129,128,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,132,
        5,6,0,0,132,133,3,42,21,0,133,17,1,0,0,0,134,137,3,24,12,0,135,137,
        3,26,13,0,136,134,1,0,0,0,136,135,1,0,0,0,137,19,1,0,0,0,138,139,
        3,48,24,0,139,21,1,0,0,0,140,141,3,26,13,0,141,23,1,0,0,0,142,143,
        5,22,0,0,143,144,5,41,0,0,144,145,5,8,0,0,145,146,3,56,28,0,146,
        147,5,10,0,0,147,148,3,48,24,0,148,25,1,0,0,0,149,150,5,41,0,0,150,
        151,5,10,0,0,151,152,3,48,24,0,152,27,1,0,0,0,153,154,5,27,0,0,154,
        155,3,42,21,0,155,156,5,28,0,0,156,157,5,5,0,0,157,158,5,41,0,0,
        158,159,5,6,0,0,159,160,3,42,21,0,160,29,1,0,0,0,161,162,5,29,0,
        0,162,163,3,48,24,0,163,167,5,3,0,0,164,166,3,32,16,0,165,164,1,
        0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,171,1,
        0,0,0,169,167,1,0,0,0,170,172,3,34,17,0,171,170,1,0,0,0,171,172,
        1,0,0,0,172,173,1,0,0,0,173,174,5,4,0,0,174,31,1,0,0,0,175,176,5,
        30,0,0,176,177,3,48,24,0,177,181,5,8,0,0,178,180,3,2,1,0,179,178,
        1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,186,
        1,0,0,0,183,181,1,0,0,0,184,185,5,31,0,0,185,187,5,7,0,0,186,184,
        1,0,0,0,186,187,1,0,0,0,187,33,1,0,0,0,188,189,5,35,0,0,189,193,
        5,8,0,0,190,192,3,2,1,0,191,190,1,0,0,0,192,195,1,0,0,0,193,191,
        1,0,0,0,193,194,1,0,0,0,194,35,1,0,0,0,195,193,1,0,0,0,196,197,5,
        32,0,0,197,198,5,41,0,0,198,200,5,5,0,0,199,201,3,38,19,0,200,199,
        1,0,0,0,200,201,1,0,0,0,201,202,1,0,0,0,202,203,5,6,0,0,203,204,
        5,8,0,0,204,205,3,56,28,0,205,206,3,42,21,0,206,37,1,0,0,0,207,212,
        3,40,20,0,208,209,5,9,0,0,209,211,3,40,20,0,210,208,1,0,0,0,211,
        214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,39,1,0,0,0,214,212,
        1,0,0,0,215,216,5,41,0,0,216,217,5,8,0,0,217,218,3,56,28,0,218,41,
        1,0,0,0,219,223,5,3,0,0,220,222,3,2,1,0,221,220,1,0,0,0,222,225,
        1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,226,1,0,0,0,225,223,
        1,0,0,0,226,227,5,4,0,0,227,43,1,0,0,0,228,229,5,34,0,0,229,230,
        5,5,0,0,230,231,3,48,24,0,231,232,5,6,0,0,232,233,5,7,0,0,233,45,
        1,0,0,0,234,239,3,48,24,0,235,236,5,9,0,0,236,238,3,48,24,0,237,
        235,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,
        47,1,0,0,0,241,239,1,0,0,0,242,243,6,24,-1,0,243,244,5,21,0,0,244,
        254,3,48,24,9,245,246,5,41,0,0,246,248,5,5,0,0,247,249,3,46,23,0,
        248,247,1,0,0,0,248,249,1,0,0,0,249,250,1,0,0,0,250,254,5,6,0,0,
        251,254,5,41,0,0,252,254,3,50,25,0,253,242,1,0,0,0,253,245,1,0,0,
        0,253,251,1,0,0,0,253,252,1,0,0,0,254,272,1,0,0,0,255,256,10,8,0,
        0,256,257,7,0,0,0,257,271,3,48,24,9,258,259,10,7,0,0,259,260,7,1,
        0,0,260,271,3,48,24,8,261,262,10,6,0,0,262,263,7,2,0,0,263,271,3,
        48,24,7,264,265,10,5,0,0,265,266,5,19,0,0,266,271,3,48,24,6,267,
        268,10,4,0,0,268,269,5,20,0,0,269,271,3,48,24,5,270,255,1,0,0,0,
        270,258,1,0,0,0,270,261,1,0,0,0,270,264,1,0,0,0,270,267,1,0,0,0,
        271,274,1,0,0,0,272,270,1,0,0,0,272,273,1,0,0,0,273,49,1,0,0,0,274,
        272,1,0,0,0,275,281,3,54,27,0,276,277,5,5,0,0,277,278,3,48,24,0,
        278,279,5,6,0,0,279,281,1,0,0,0,280,275,1,0,0,0,280,276,1,0,0,0,
        281,51,1,0,0,0,282,283,7,3,0,0,283,53,1,0,0,0,284,285,7,4,0,0,285,
        55,1,0,0,0,286,287,7,5,0,0,287,57,1,0,0,0,22,62,79,99,110,121,125,
        129,136,167,171,181,186,193,200,212,223,239,248,253,270,272,280
    ]

class MyLangParser ( Parser ):

    grammarFileName = "MyLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<='", "'>='", "'{'", "'}'", "'('", "')'", 
                     "';'", "':'", "','", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'<'", "'>'", "'=='", "'!='", "'&&'", "'||'", "'!'", 
                     "'let'", "'if'", "'else'", "'while'", "'for'", "'try'", 
                     "'catch'", "'match'", "'case'", "'break'", "'function'", 
                     "'return'", "'print'", "'default'", "'int'", "'float'", 
                     "'string'", "'bool'", "'void'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "LBRACE", "RBRACE", 
                      "LPAREN", "RPAREN", "SEMI", "COLON", "COMMA", "ASSIGN", 
                      "PLUS", "MINUS", "STAR", "SLASH", "LT", "GT", "EQ", 
                      "NEQ", "AND", "OR", "NOT", "LET", "IF", "ELSE", "WHILE", 
                      "FOR", "TRY", "CATCH", "MATCH", "CASE", "BREAK", "FUNCTION", 
                      "RETURN", "PRINT", "DEFAULT", "INT", "FLOAT", "STRING", 
                      "BOOL", "VOID", "ID", "INT_LITERAL", "FLOAT_LITERAL", 
                      "STRING_LITERAL", "BOOL_LITERAL", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_varDeclaration = 2
    RULE_assignment = 3
    RULE_expressionStatement = 4
    RULE_returnStatement = 5
    RULE_ifStatement = 6
    RULE_whileStatement = 7
    RULE_forStatement = 8
    RULE_forInit = 9
    RULE_forCondition = 10
    RULE_forUpdate = 11
    RULE_varDeclarationWithoutSemi = 12
    RULE_assignmentWithoutSemi = 13
    RULE_tryCatchStatement = 14
    RULE_matchStatement = 15
    RULE_matchCase = 16
    RULE_defaultCase = 17
    RULE_functionDeclaration = 18
    RULE_paramList = 19
    RULE_param = 20
    RULE_block = 21
    RULE_printStatement = 22
    RULE_argList = 23
    RULE_expression = 24
    RULE_primary = 25
    RULE_binaryOp = 26
    RULE_literal = 27
    RULE_type = 28

    ruleNames =  [ "program", "statement", "varDeclaration", "assignment", 
                   "expressionStatement", "returnStatement", "ifStatement", 
                   "whileStatement", "forStatement", "forInit", "forCondition", 
                   "forUpdate", "varDeclarationWithoutSemi", "assignmentWithoutSemi", 
                   "tryCatchStatement", "matchStatement", "matchCase", "defaultCase", 
                   "functionDeclaration", "paramList", "param", "block", 
                   "printStatement", "argList", "expression", "primary", 
                   "binaryOp", "literal", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    LBRACE=3
    RBRACE=4
    LPAREN=5
    RPAREN=6
    SEMI=7
    COLON=8
    COMMA=9
    ASSIGN=10
    PLUS=11
    MINUS=12
    STAR=13
    SLASH=14
    LT=15
    GT=16
    EQ=17
    NEQ=18
    AND=19
    OR=20
    NOT=21
    LET=22
    IF=23
    ELSE=24
    WHILE=25
    FOR=26
    TRY=27
    CATCH=28
    MATCH=29
    CASE=30
    BREAK=31
    FUNCTION=32
    RETURN=33
    PRINT=34
    DEFAULT=35
    INT=36
    FLOAT=37
    STRING=38
    BOOL=39
    VOID=40
    ID=41
    INT_LITERAL=42
    FLOAT_LITERAL=43
    STRING_LITERAL=44
    BOOL_LITERAL=45
    WS=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MyLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MyLangParser.RBRACE, 0)

        def EOF(self):
            return self.getToken(MyLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MyLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(MyLangParser.LBRACE)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68200572125216) != 0):
                self.state = 59
                self.statement()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(MyLangParser.RBRACE)
            self.state = 66
            self.match(MyLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclaration(self):
            return self.getTypedRuleContext(MyLangParser.VarDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MyLangParser.AssignmentContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(MyLangParser.FunctionDeclarationContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MyLangParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MyLangParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MyLangParser.ForStatementContext,0)


        def tryCatchStatement(self):
            return self.getTypedRuleContext(MyLangParser.TryCatchStatementContext,0)


        def matchStatement(self):
            return self.getTypedRuleContext(MyLangParser.MatchStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MyLangParser.ReturnStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(MyLangParser.PrintStatementContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MyLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.varDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.functionDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.expressionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.ifStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.whileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.forStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.tryCatchStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 76
                self.matchStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 77
                self.returnStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 78
                self.printStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(MyLangParser.LET, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def COLON(self):
            return self.getToken(MyLangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(MyLangParser.TypeContext,0)


        def ASSIGN(self):
            return self.getToken(MyLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = MyLangParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(MyLangParser.LET)
            self.state = 82
            self.match(MyLangParser.ID)
            self.state = 83
            self.match(MyLangParser.COLON)
            self.state = 84
            self.type_()
            self.state = 85
            self.match(MyLangParser.ASSIGN)
            self.state = 86
            self.expression(0)
            self.state = 87
            self.match(MyLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MyLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MyLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(MyLangParser.ID)
            self.state = 90
            self.match(MyLangParser.ASSIGN)
            self.state = 91
            self.expression(0)
            self.state = 92
            self.match(MyLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = MyLangParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.expression(0)
            self.state = 95
            self.match(MyLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MyLangParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MyLangParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(MyLangParser.RETURN)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68169723019296) != 0):
                self.state = 98
                self.expression(0)


            self.state = 101
            self.match(MyLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MyLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(MyLangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(MyLangParser.ELSE, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MyLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(MyLangParser.IF)
            self.state = 104
            self.match(MyLangParser.LPAREN)
            self.state = 105
            self.expression(0)
            self.state = 106
            self.match(MyLangParser.RPAREN)
            self.state = 107
            self.block()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 108
                self.match(MyLangParser.ELSE)
                self.state = 109
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MyLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = MyLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(MyLangParser.WHILE)
            self.state = 113
            self.match(MyLangParser.LPAREN)
            self.state = 114
            self.expression(0)
            self.state = 115
            self.match(MyLangParser.RPAREN)
            self.state = 116
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MyLangParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.SEMI)
            else:
                return self.getToken(MyLangParser.SEMI, i)

        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def forInit(self):
            return self.getTypedRuleContext(MyLangParser.ForInitContext,0)


        def forCondition(self):
            return self.getTypedRuleContext(MyLangParser.ForConditionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(MyLangParser.ForUpdateContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MyLangParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(MyLangParser.FOR)
            self.state = 119
            self.match(MyLangParser.LPAREN)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22 or _la==41:
                self.state = 120
                self.forInit()


            self.state = 123
            self.match(MyLangParser.SEMI)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68169723019296) != 0):
                self.state = 124
                self.forCondition()


            self.state = 127
            self.match(MyLangParser.SEMI)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 128
                self.forUpdate()


            self.state = 131
            self.match(MyLangParser.RPAREN)
            self.state = 132
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclarationWithoutSemi(self):
            return self.getTypedRuleContext(MyLangParser.VarDeclarationWithoutSemiContext,0)


        def assignmentWithoutSemi(self):
            return self.getTypedRuleContext(MyLangParser.AssignmentWithoutSemiContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = MyLangParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forInit)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.varDeclarationWithoutSemi()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.assignmentWithoutSemi()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_forCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCondition" ):
                listener.enterForCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCondition" ):
                listener.exitForCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = MyLangParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentWithoutSemi(self):
            return self.getTypedRuleContext(MyLangParser.AssignmentWithoutSemiContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = MyLangParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.assignmentWithoutSemi()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationWithoutSemiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(MyLangParser.LET, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def COLON(self):
            return self.getToken(MyLangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(MyLangParser.TypeContext,0)


        def ASSIGN(self):
            return self.getToken(MyLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_varDeclarationWithoutSemi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclarationWithoutSemi" ):
                listener.enterVarDeclarationWithoutSemi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclarationWithoutSemi" ):
                listener.exitVarDeclarationWithoutSemi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclarationWithoutSemi" ):
                return visitor.visitVarDeclarationWithoutSemi(self)
            else:
                return visitor.visitChildren(self)




    def varDeclarationWithoutSemi(self):

        localctx = MyLangParser.VarDeclarationWithoutSemiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varDeclarationWithoutSemi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(MyLangParser.LET)
            self.state = 143
            self.match(MyLangParser.ID)
            self.state = 144
            self.match(MyLangParser.COLON)
            self.state = 145
            self.type_()
            self.state = 146
            self.match(MyLangParser.ASSIGN)
            self.state = 147
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentWithoutSemiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MyLangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_assignmentWithoutSemi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentWithoutSemi" ):
                listener.enterAssignmentWithoutSemi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentWithoutSemi" ):
                listener.exitAssignmentWithoutSemi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentWithoutSemi" ):
                return visitor.visitAssignmentWithoutSemi(self)
            else:
                return visitor.visitChildren(self)




    def assignmentWithoutSemi(self):

        localctx = MyLangParser.AssignmentWithoutSemiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignmentWithoutSemi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(MyLangParser.ID)
            self.state = 150
            self.match(MyLangParser.ASSIGN)
            self.state = 151
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryCatchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(MyLangParser.TRY, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(MyLangParser.BlockContext,i)


        def CATCH(self):
            return self.getToken(MyLangParser.CATCH, 0)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_tryCatchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryCatchStatement" ):
                listener.enterTryCatchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryCatchStatement" ):
                listener.exitTryCatchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryCatchStatement" ):
                return visitor.visitTryCatchStatement(self)
            else:
                return visitor.visitChildren(self)




    def tryCatchStatement(self):

        localctx = MyLangParser.TryCatchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_tryCatchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MyLangParser.TRY)
            self.state = 154
            self.block()
            self.state = 155
            self.match(MyLangParser.CATCH)
            self.state = 156
            self.match(MyLangParser.LPAREN)
            self.state = 157
            self.match(MyLangParser.ID)
            self.state = 158
            self.match(MyLangParser.RPAREN)
            self.state = 159
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATCH(self):
            return self.getToken(MyLangParser.MATCH, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(MyLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MyLangParser.RBRACE, 0)

        def matchCase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.MatchCaseContext)
            else:
                return self.getTypedRuleContext(MyLangParser.MatchCaseContext,i)


        def defaultCase(self):
            return self.getTypedRuleContext(MyLangParser.DefaultCaseContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_matchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchStatement" ):
                listener.enterMatchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchStatement" ):
                listener.exitMatchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchStatement" ):
                return visitor.visitMatchStatement(self)
            else:
                return visitor.visitChildren(self)




    def matchStatement(self):

        localctx = MyLangParser.MatchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_matchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MyLangParser.MATCH)
            self.state = 162
            self.expression(0)
            self.state = 163
            self.match(MyLangParser.LBRACE)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 164
                self.matchCase()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 170
                self.defaultCase()


            self.state = 173
            self.match(MyLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(MyLangParser.CASE, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(MyLangParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def BREAK(self):
            return self.getToken(MyLangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_matchCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchCase" ):
                listener.enterMatchCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchCase" ):
                listener.exitMatchCase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchCase" ):
                return visitor.visitMatchCase(self)
            else:
                return visitor.visitChildren(self)




    def matchCase(self):

        localctx = MyLangParser.MatchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_matchCase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(MyLangParser.CASE)
            self.state = 176
            self.expression(0)
            self.state = 177
            self.match(MyLangParser.COLON)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68200572125216) != 0):
                self.state = 178
                self.statement()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 184
                self.match(MyLangParser.BREAK)
                self.state = 185
                self.match(MyLangParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(MyLangParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(MyLangParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_defaultCase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultCase" ):
                listener.enterDefaultCase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultCase" ):
                listener.exitDefaultCase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultCase" ):
                return visitor.visitDefaultCase(self)
            else:
                return visitor.visitChildren(self)




    def defaultCase(self):

        localctx = MyLangParser.DefaultCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_defaultCase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(MyLangParser.DEFAULT)
            self.state = 189
            self.match(MyLangParser.COLON)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68200572125216) != 0):
                self.state = 190
                self.statement()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(MyLangParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(MyLangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(MyLangParser.TypeContext,0)


        def block(self):
            return self.getTypedRuleContext(MyLangParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(MyLangParser.ParamListContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = MyLangParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MyLangParser.FUNCTION)
            self.state = 197
            self.match(MyLangParser.ID)
            self.state = 198
            self.match(MyLangParser.LPAREN)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 199
                self.paramList()


            self.state = 202
            self.match(MyLangParser.RPAREN)
            self.state = 203
            self.match(MyLangParser.COLON)
            self.state = 204
            self.type_()
            self.state = 205
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.COMMA)
            else:
                return self.getToken(MyLangParser.COMMA, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MyLangParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.param()
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 208
                self.match(MyLangParser.COMMA)
                self.state = 209
                self.param()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def COLON(self):
            return self.getToken(MyLangParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(MyLangParser.TypeContext,0)


        def getRuleIndex(self):
            return MyLangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MyLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MyLangParser.ID)
            self.state = 216
            self.match(MyLangParser.COLON)
            self.state = 217
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MyLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MyLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MyLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(MyLangParser.LBRACE)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68200572125216) != 0):
                self.state = 220
                self.statement()
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 226
            self.match(MyLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(MyLangParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MyLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = MyLangParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MyLangParser.PRINT)
            self.state = 229
            self.match(MyLangParser.LPAREN)
            self.state = 230
            self.expression(0)
            self.state = 231
            self.match(MyLangParser.RPAREN)
            self.state = 232
            self.match(MyLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyLangParser.COMMA)
            else:
                return self.getToken(MyLangParser.COMMA, i)

        def getRuleIndex(self):
            return MyLangParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = MyLangParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.expression(0)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 235
                self.match(MyLangParser.COMMA)
                self.state = 236
                self.expression(0)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyLangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprPrimaryContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(MyLangParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPrimary" ):
                listener.enterExprPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPrimary" ):
                listener.exitExprPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPrimary" ):
                return visitor.visitExprPrimary(self)
            else:
                return visitor.visitChildren(self)


    class ExprAddSubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(MyLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(MyLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAddSub" ):
                listener.enterExprAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAddSub" ):
                listener.exitExprAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAddSub" ):
                return visitor.visitExprAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ExprComparisonContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(MyLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(MyLangParser.NEQ, 0)
        def LT(self):
            return self.getToken(MyLangParser.LT, 0)
        def GT(self):
            return self.getToken(MyLangParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprComparison" ):
                listener.enterExprComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprComparison" ):
                listener.exitExprComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprComparison" ):
                return visitor.visitExprComparison(self)
            else:
                return visitor.visitChildren(self)


    class ExprIdentifierContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprIdentifier" ):
                listener.enterExprIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprIdentifier" ):
                listener.exitExprIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprIdentifier" ):
                return visitor.visitExprIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class ExprFunctionCallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MyLangParser.ID, 0)
        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)
        def argList(self):
            return self.getTypedRuleContext(MyLangParser.ArgListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprFunctionCall" ):
                listener.enterExprFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprFunctionCall" ):
                listener.exitExprFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprFunctionCall" ):
                return visitor.visitExprFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class ExprMulDivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def STAR(self):
            return self.getToken(MyLangParser.STAR, 0)
        def SLASH(self):
            return self.getToken(MyLangParser.SLASH, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMulDiv" ):
                listener.enterExprMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMulDiv" ):
                listener.exitExprMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMulDiv" ):
                return visitor.visitExprMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class ExprNotContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MyLangParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprNot" ):
                listener.enterExprNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprNot" ):
                listener.exitExprNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNot" ):
                return visitor.visitExprNot(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicalOrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(MyLangParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLogicalOr" ):
                listener.enterExprLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLogicalOr" ):
                listener.exitExprLogicalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLogicalOr" ):
                return visitor.visitExprLogicalOr(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicalAndContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyLangParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(MyLangParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLogicalAnd" ):
                listener.enterExprLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLogicalAnd" ):
                listener.exitExprLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLogicalAnd" ):
                return visitor.visitExprLogicalAnd(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = MyLangParser.ExprNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 243
                self.match(MyLangParser.NOT)
                self.state = 244
                self.expression(9)
                pass

            elif la_ == 2:
                localctx = MyLangParser.ExprFunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 245
                self.match(MyLangParser.ID)
                self.state = 246
                self.match(MyLangParser.LPAREN)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68169723019296) != 0):
                    self.state = 247
                    self.argList()


                self.state = 250
                self.match(MyLangParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = MyLangParser.ExprIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 251
                self.match(MyLangParser.ID)
                pass

            elif la_ == 4:
                localctx = MyLangParser.ExprPrimaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 252
                self.primary()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 270
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = MyLangParser.ExprMulDivContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 255
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 256
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 257
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = MyLangParser.ExprAddSubContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 258
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 259
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 260
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = MyLangParser.ExprComparisonContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 261
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 262
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491526) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 263
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = MyLangParser.ExprLogicalAndContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 264
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 265
                        self.match(MyLangParser.AND)
                        self.state = 266
                        self.expression(6)
                        pass

                    elif la_ == 5:
                        localctx = MyLangParser.ExprLogicalOrContext(self, MyLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 267
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 268
                        self.match(MyLangParser.OR)
                        self.state = 269
                        self.expression(5)
                        pass

             
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MyLangParser.LiteralContext,0)


        def LPAREN(self):
            return self.getToken(MyLangParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MyLangParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MyLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = MyLangParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primary)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42, 43, 44, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.literal()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(MyLangParser.LPAREN)
                self.state = 277
                self.expression(0)
                self.state = 278
                self.match(MyLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(MyLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MyLangParser.MINUS, 0)

        def STAR(self):
            return self.getToken(MyLangParser.STAR, 0)

        def SLASH(self):
            return self.getToken(MyLangParser.SLASH, 0)

        def LT(self):
            return self.getToken(MyLangParser.LT, 0)

        def GT(self):
            return self.getToken(MyLangParser.GT, 0)

        def EQ(self):
            return self.getToken(MyLangParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MyLangParser.NEQ, 0)

        def AND(self):
            return self.getToken(MyLangParser.AND, 0)

        def OR(self):
            return self.getToken(MyLangParser.OR, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_binaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)




    def binaryOp(self):

        localctx = MyLangParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2095104) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(MyLangParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(MyLangParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(MyLangParser.STRING_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(MyLangParser.BOOL_LITERAL, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MyLangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65970697666560) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MyLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MyLangParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MyLangParser.STRING, 0)

        def BOOL(self):
            return self.getToken(MyLangParser.BOOL, 0)

        def VOID(self):
            return self.getToken(MyLangParser.VOID, 0)

        def getRuleIndex(self):
            return MyLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MyLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303778816) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




