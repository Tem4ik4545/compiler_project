from src.IR.ir_generator import IRGenerator
from src.optimizer.ir_optimizer import IROptimizer
from src.Nasm.nasm_generator import NASMGenerator
from src.AST.ASTBuilder import ASTBuilder
from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser
from antlr4 import InputStream, CommonTokenStream


def run_nasm_test(code: str, description: str):
    print(f"\n=== Тест NASM: {description} ===")
    input_stream = InputStream(code)
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)
    tree = parser.program()

    ast = ASTBuilder().visit(tree)
    ir = IRGenerator().generate(ast)
    optimized_ir = IROptimizer().optimize(ir)

    nasm_code = NASMGenerator().generate(optimized_ir)
    print("\n--- Сгенерированный NASM код ---")
    print(nasm_code)


def main():
    tests = [
        ("Простой арифметический пример", '''
        {
            let x: int = 5;
            let y: int = 10;
            let z: int = x + y;
            print(z);
        }
        '''),

        ("Условный оператор if-else", '''
        {
            let x: int = 5;
            if (x < 10) {
                print(x);
            } else {
                print(0);
            }
        }
        '''),

        ("Цикл while", '''
        {
            let x: int = 0;
            while (x < 3) {
                print(x);
                x = x + 1;
            }
        }
        '''),

        ("Цикл for", '''
        {
            for (let i: int = 0; i < 3; i = i + 1) {
                print(i);
            }
        }
        '''),

        ("Функция и вызов", '''
        {
            function sum(a: int, b: int): int {
                return a + b;
            }
            let res: int = sum(2, 3);
            print(res);
        }
        '''),

        ("Обработка исключений try/catch", '''
        {
            try {
                print(1);
            } catch (e) {
                print(0);
            }
        }
        '''),

        ("Match-case конструкция", '''
        {
            let x: int = 2;
            match x {
                case 1: print(1);
                case 2: print(2);
                default: print(0);
            }
        }
        '''),

        ("Логические выражения", '''
        {
            let a: bool = true;
            let b: bool = false;
            if (a && !b || false) {
                print(1);
            }
        }
        '''),

        ("Функция с вычислением и вложенными вызовами", '''
        {
            function mul(a: int, b: int): int {
                return a * b;
            }
            function sum(a: int, b: int): int {
                return a + b;
            }
            let total: int = sum(mul(2, 3), 4);
            print(total);
        }
        '''),

        ("Функция с более чем 6 аргументами", '''
        {
            function total(a: int, b: int, c: int, d: int, e: int, f: int, g: int): int {
                return a + b + c + d + e + f + g;
            }
            let res: int = total(1, 2, 3, 4, 5, 6, 7);
            print(res);
        }
        '''),

        ("Печать строки", '''
        {
            print("Hello, NASM!");
        }
        ''')
    ]

    for desc, code in tests:
        run_nasm_test(code, desc)


if __name__ == "__main__":
    main()
