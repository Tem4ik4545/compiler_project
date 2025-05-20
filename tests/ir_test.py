from antlr4 import *
from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser
from src.AST.ASTBuilder import ASTBuilder
from src.IR.ir_generator import IRGenerator


def run_ir_test(code: str, description: str):
    print(f"\n=== Тест IR: {description} ===")
    input_stream = InputStream(code)
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)

    tree = parser.program()
    print("\n--- Дерево синтаксического анализа ---")
    print(tree.toStringTree(recog=parser))

    visitor = ASTBuilder()
    ast = visitor.visit(tree)
    print("\n--- Построенное AST ---")
    print(ast)

    ir_gen = IRGenerator()
    try:
        ir = ir_gen.generate(ast)
        print("\n--- Сгенерированный трёхадресный код (IR) ---")
        for instr in ir:
            print(instr)
    except Exception as e:
        print("❌ Ошибка генерации IR:", e)


def main():
    code = r'''
    {

        let m: float = 3.1415926;
        v = m + 1;
        
        let a: bool = true;
        let b: bool = false;
        if (a && !b || false) {
            print("ok");
        }

        let x: int = 0;
        while (x < 3) {
            x = x + 1;
            print(x);
        }

        for (let i: int = 0; i < 3; i = i + 1) {
            print(i);
        }

        try {
            print("try");
        } catch (e) {
            print("catch");
        }

        match x {
            case 1: print("one");
            case 2: print("two");
            default: print("other");
        }

        function sum(a: int, b: int): int {
            return a + b;
        }

        print(sum(2, 3));
        
        function add(a: int, b: int): int {
        return a + b;
        }

        let res: int = add(7, 8);
        print(res);
    }
    '''

    run_ir_test(code, "Полный тест конструкций")


if __name__ == "__main__":
    main()
