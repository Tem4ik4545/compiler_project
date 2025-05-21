import sys
from antlr4 import *
from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser
from src.AST.ASTBuilder import ASTBuilder
from src.IR.ir_generator import IRGenerator
from src.optimizer.ir_optimizer import IROptimizer


def normalize_lines(lines):
    return [line.strip() for line in lines if line.strip()]


def run_ir_test(code: str, expected_ir: str, description: str) -> bool:
    print(f"\n=== Тест IR: {description} ===")

    # Лексер и парсер
    input_stream = InputStream(code)
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)

    # AST
    tree = parser.program()
    ast = ASTBuilder().visit(tree)

    # Генерация IR
    ir_gen = IRGenerator()
    ir = ir_gen.generate(ast)

    print("=== 🧾 IR до оптимизации ===")
    for instr in ir:
        print(instr)
    print()

    # Оптимизация
    optimizer = IROptimizer()
    optimized_ir = optimizer.optimize(ir)

    print("=== 🧾 IR после оптимизации ===")
    for instr in optimized_ir:
        print(instr)
    print()

    # Нормализация строк для сравнения
    ir_lines = normalize_lines([str(instr) for instr in optimized_ir])
    expected_lines = normalize_lines(expected_ir.splitlines())

    print("\n--- Оптимизированный IR ---")
    print("\n".join(ir_lines))
    print("\n--- Ожидаемый IR ---")
    print("\n".join(expected_lines))

    # Сравнение
    if ir_lines == expected_lines:
        print("\n✅ IR совпадает с эталонным.")
        return True
    else:
        print("\n❌ IR не совпадает с эталонным!")
        return False


def main():
    tests = [
        (
            """
            {
                let x: int = 1 + 2;
                print(x);
            }
            """,
            """
            t0 = 1 + 2
            x = t0
            print x
            """,
            "Свёртка констант (constant folding)"
        ),
        (
            """
            {
                let a: int = 1;
                let b: int = a;
                let c: int = b;
                print(c);
            }
            """,
            """
            a = 1
            b = a
            c = b
            print c
            """,
            "Copy propagation (одно звено)"
        ),
        (
            """
            {
                let t1: int = 10;
                let t2: int = t1;
                let x: int = 1;
                print(x);
            }
            """,
            """
            t1 = 10
            x = 1
            print x
            """,
            "Удаление неиспользуемых временных переменных"
        ),
        (
            """
            {
                let x: int = 5;
                x = x;
                print(x);
            }
            """,
            """
            x = 5
            print x
            """,
            "Удаление самоприсваивания"
        ),
        (
            """
            {
                if (true) {
                    print("ok");
                }
            }
            """,
            """
            t0 = !True
            if t0 goto else_0
            print "ok"
            goto endif_1
            else_0:
            endif_1:
            """,
            "simplify_if_true: if (true)"
        ),
        (
            """
            {
                if (false) {
                    print("no");
                }
            }
            """,
            """
            t0 = !False
            if t0 goto else_0
            print "no"
            goto endif_1
            else_0:
            endif_1:
            """,
            "simplify_if_true: if (false)"
        ),
        (
            """
            {
                let x: bool = !true;
                if (!x) {
                    print("never");
                }
            }
            """,
            """
            t0 = !True
            x = t0
            t1 = !x
            t2 = !t1
            if t2 goto else_0
            print "never"
            goto endif_1
            else_0:
            endif_1:
            """,
            "simplify_if_true: x = !true; if (!x)"
        ),
        (
            """
            {
                function test(): int {
                    return 42;
                    print("dead");
                }
            }
            """,
            """
            func_test:
            params:
            return 42
            ; end func_test
            """,
            "Удаление мёртвого кода после return"
        )
    ]

    passed = 0
    for code, expected, description in tests:
        if run_ir_test(code, expected, description):
            passed += 1

    print(f"\n=== Результат: {passed}/{len(tests)} тестов успешно пройдены ===")


if __name__ == "__main__":
    main()
