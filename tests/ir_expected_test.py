import sys
from antlr4 import *
from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser
from src.AST.ASTBuilder import ASTBuilder
from src.IR.ir_generator import IRGenerator


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

    # IR
    ir_gen = IRGenerator()
    ir = ir_gen.generate(ast)

    # Генерация строки IR
    ir_lines = [str(instr) for instr in ir]
    ir_str = "\n".join(ir_lines).strip()
    expected_ir = expected_ir.strip()

    # Вывод сырого IR
    print("\n--- Сгенерированный IR ---")
    print(ir_str)

    # Эталон
    print("\n--- Эталонный IR ---")
    print(expected_ir)

    # Сравнение
    if ir_str == expected_ir:
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
                let x: int = 1;
                print(x);
            }
            """,
            """
x = 1
print x
            """,
            "Простой let + print"
        ),
        (
            """
            {
                if (true) {
                    print("yes");
                }
            }
            """,
            """
if !True goto else_0
print yes
goto endif_1
else_0:
endif_1:
            """,
            "if без else"
        ),
        (
            """
            {
                let x: int = 0;
                while (x < 3) {
                    print(x);
                    x = x + 1;
                }
            }
            """,
            """
x = 0
while_start_0:
t0 = x < 3
if !t0 goto while_end_1
print x
t1 = x + 1
x = t1
goto while_start_0
while_end_1:
            """,
            "while loop"
        ),
        (
            """
            {
                for (let i: int = 0; i < 2; i = i + 1) {
                    print(i);
                }
            }
            """,
            """
i = 0
for_start_0:
t0 = i < 2
if !t0 goto for_end_1
print i
t1 = i + 1
i = t1
goto for_start_0
for_end_1:
            """,
            "for loop"
        ),
        (
            """
            {
                function sum(a: int, b: int): int {
                    return a + b;
                }
                print(sum(1, 2));
            }
            """,
            """
func_sum:
t0 = a + b
return t0
t1 = call sum(1, 2)
print t1
            """,
            "function + call"
        ),
        (
            """
            {
                try {
                    print("ok");
                } catch (e) {
                    print("err");
                }
            }
            """,
            """
try_0:
print ok
goto end_try_2
catch_1:
print err
end_try_2:
            """,
            "try / catch"
        ),
        (
            """
            {
                let x: int = 2;
                match x {
                    case 1: print("one");
                    case 2: print("two");
                    default: print("other");
                }
            }
            """,
            """
x = 2
t0 = x == 1
if t0 goto case_0_1
t1 = x == 2
if t1 goto case_1_2
goto default_case_3
case_0_1:
print one
goto end_match_0
case_1_2:
print two
goto end_match_0
default_case_3:
print other
end_match_0:
            """,
            "match-case"
        )
    ]

    passed = 0
    for code, expected, description in tests:
        if run_ir_test(code, expected, description):
            passed += 1

    print(f"\n=== Результат: {passed}/{len(tests)} тестов успешно пройдены ===")


if __name__ == "__main__":
    main()
