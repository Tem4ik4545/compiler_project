import sys
from antlr4 import *
from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser
from src.AST.ASTBuilder import ASTBuilder

def parse_code(code: str):
    input_stream = InputStream(code)
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)

    tree = parser.program()
    print("\n### Разобранное дерево синтаксического анализа ###")
    print(tree.toStringTree(recog=parser))

    visitor = ASTBuilder()
    ast = visitor.visitProgram(tree)
    print("\n### Построенное AST ###")
    print(ast)


code = r"""
{
    
    let x: int = 5;
    print(x);

    
    if (x < 10) {
        print("x is less than 10");
    } else {
        print("x is 10 or more");
    }

    
    while (x < 8) {
        x = x + 1;
        print(x);
    }

    
    for (let i: int = 0; i < 5; i = i + 1) {
        print(i);
    }

    
    try {
        print("Inside try");
    } catch (e) {
        print("Error: " + e);
    }

    
    match x {
        case 5: print("x equals 5");
        default: print("x is something else");
    }

    
    function add(a: int, b: int): int {
        return a + b;
    }

    
    print(add(3, 4));
}
"""

if __name__ == "__main__":
    parse_code(code)
