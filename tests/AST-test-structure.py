import unittest
from antlr4 import InputStream, CommonTokenStream
from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser
from src.AST.ASTBuilder import ASTBuilder
from src.AST.Karkas import *

def build_ast(code: str):
    input_stream = InputStream(code)
    lexer = MyLangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MyLangParser(tokens)
    tree = parser.program()
    visitor = ASTBuilder()
    return visitor.visitProgram(tree)

class TestAST(unittest.TestCase):

    def test_var_declaration_and_print(self):
        code = """
        {
            let x: int = 5;
            print(x);
        }
        """
        ast = build_ast(code)
        self.assertIsInstance(ast, Program)
        self.assertEqual(len(ast.statements), 2)
        self.assertIsInstance(ast.statements[0], VarDeclaration)
        self.assertIsInstance(ast.statements[1], PrintStatement)

    def test_if_else(self):
        code = """
        {
            if (1 < 2) {
                print("ok");
            } else {
                print("fail");
            }
        }
        """
        ast = build_ast(code)
        stmt = ast.statements[0]
        self.assertIsInstance(stmt, IfStatement)
        self.assertIsNotNone(stmt.then_block)
        self.assertIsNotNone(stmt.else_block)

    def test_while(self):
        code = """
        {
            while (x < 10) {
                print(x);
            }
        }
        """
        ast = build_ast(code)
        stmt = ast.statements[0]
        self.assertIsInstance(stmt, WhileStatement)

    def test_for(self):
        code = """
        {
            for (let i: int = 0; i < 5; i = i + 1) {
                print(i);
            }
        }
        """
        ast = build_ast(code)
        stmt = ast.statements[0]
        self.assertIsInstance(stmt, ForStatement)

    def test_try_catch(self):
        code = """
        {
            try {
                print("try");
            } catch (e) {
                print("error");
            }
        }
        """
        ast = build_ast(code)
        stmt = ast.statements[0]
        self.assertIsInstance(stmt, TryCatchStatement)

    def test_match(self):
        code = """
        {
            match x {
                case 1: print("one");
                default: print("other");
            }
        }
        """
        ast = build_ast(code)
        stmt = ast.statements[0]
        self.assertIsInstance(stmt, MatchStatement)
        self.assertEqual(len(stmt.cases), 1)
        self.assertIsInstance(stmt.default, DefaultCase)

    def test_function_decl_and_call(self):
        code = """
        {
            function add(a: int, b: int): int {
                return a + b;
            }
            print(add(3, 4));
        }
        """
        ast = build_ast(code)
        self.assertEqual(len(ast.statements), 2)
        self.assertIsInstance(ast.statements[0], FunctionDeclaration)
        self.assertIsInstance(ast.statements[1], PrintStatement)
        self.assertIsInstance(ast.statements[1].expression, FunctionCall)

if __name__ == '__main__':
    unittest.main()
