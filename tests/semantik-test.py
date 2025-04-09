import sys
from antlr4 import *
from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser
from src.AST.ASTBuilder import ASTBuilder
from src.semantic.semantic_analyzer import SemanticAnalyzer


def run_test(code: str, description: str, should_fail=False) -> bool:
    print(f"\n=== Тест: {description} ===")
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

    analyzer = SemanticAnalyzer()
    try:
        analyzer.analyze(ast)
        print("✅ Семантический анализ пройден успешно!")
        return not should_fail
    except Exception as e:
        print(f"❌ Ошибка семантического анализа: {e}")
        return should_fail


def main():
    tests = [
        (r'''
        {
            let x: int = 5;
            print(x);
        }
        ''', "Корректный код", False),

        (r'''
        {
            print(y);
        }
        ''', "Необъявленная переменная", True),

        (r'''
        {
            let x: int = 5;
            x = "hello";
        }
        ''', "Несовместимость типов", True),

        (r'''
        {
            let x: int = 5;
            let x: int = 10;
            print(x);
        }
        ''', "Дублирование объявления переменной", True),

        (r'''
        {
            function add(a: int, b: int): int {
                return a + b;
            }
            print(add(3));
        }
        ''', "Ошибка вызова функции (недостаточно аргументов)", True),

        (r'''
        {
            if (true) {
                print("yes");
            } else {
                print("no");
            }
        }
        ''', "Условный оператор (if/else)", False),

        (r'''
        {
            let x: int = 0;
            while (x < 3) {
                x = x + 1;
            }
        }
        ''', "Цикл while", False),

        (r'''
        {
            for (let i: int = 0; i < 3; i = i + 1) {
                print(i);
            }
        }
        ''', "Цикл for", False),

        (r'''
        {
            try {
                print("try block");
            } catch (e) {
                print("catch block");
            }
        }
        ''', "try/catch", False),

        (r'''
        {
            let x: int = 2;
            match x {
                case 1: print("one");
                case 2: print("two");
                default: print("other");
            }
        }
        ''', "match-case", False),

        (r'''
        {
            function sum(a: int, b: int): int {
                return a + b;
            }
            print(sum(2, 3));
        }
        ''', "Корректный вызов функции", False),

        (r'''
                {
                    let a: bool = true;
                    let b: bool = false;
                    if (a && !b || false) {
                        print("ok");
                    }
                }
                ''', "Логические операции (&&, ||, !)", False),

        (r'''
                {
                    let x: int = 5;
                    let y: string = "hello";
                    if (x < y) {
                        print("fail");
                    }
                }
                ''', "Сравнение несовместимых типов (int < string)", True),
        (r'''
        {
            let x: int = 5;
            let y: string = "hi";
            if (x == y) {
                print("fail");
            }
        }
        ''', "Сравнение int == string", True),

        (r'''
        {
            let x: bool = true;
            let y: int = 10;
            if (x != y) {
                print("fail");
            }
        }
        ''', "Сравнение bool != int", True),

        (r'''
        {
            let x: float = 1.5;
            let y: bool = false;
            if (x < y) {
                print("fail");
            }
        }
        ''', "Сравнение float < bool", True),

        (r'''
        {
            let a: string = "a";
            let b: bool = true;
            if (a > b) {
                print("fail");
            }
        }
        ''', "Сравнение string > bool", True),

        (r'''
        {
            let name: string = "John";
            if (name < 3) {
                print("fail");
            }
        }
        ''', "Сравнение string < int", True),
        (r'''
        {
            if (5) {
                print("fail");
            }
        }
        ''', "if с условием не bool", True),

        # WHILE: условие — не bool
        (r'''
        {
            while ("nope") {
                print("fail");
            }
        }
        ''', "while с условием не bool", True),

        # FOR: init — не int
        (r'''
        {
            for (let i: string = "str"; i < 3; i = i + 1) {
                print(i);
            }
        }
        ''', "for с нечисловым init", True),

        # FOR: condition — не bool
        (r'''
        {
            for (let i: int = 0; "str"; i = i + 1) {
                print(i);
            }
        }
        ''', "for с некорректным условием (не bool)", True),

        # FOR: update — несовместимый тип
        (r'''
        {
            for (let i: int = 0; i < 3; i = "oops") {
                print(i);
            }
        }
        ''', "for с некорректным update", True),

        # TRY/CATCH: catch переменная уже существует
        (r'''
        {
            let e: int = 0;
            try {
                print("try");
            } catch (e) {
                print("catch");
            }
        }
        ''', "catch переменная уже объявлена", True),

        # MATCH: выражение и case разных типов
        (r'''
        {
            let x: int = 1;
            match x {
                case "str": print("fail");
                default: print("ok");
            }
        }
        ''', "match: case не совпадает по типу с выражением", True),

        # RETURN: возврат другого типа
        (r'''
        {
            function f(): int {
                return "str";
            }
        }
        ''', "return с типом, отличным от объявленного", True),

        # FUNCTION: повторное объявление параметров
        (r'''
        {
            function f(x: int, x: string): int {
                return 1;
            }
        }
        ''', "функция с дублирующими параметрами", True),
    ]

    passed = 0
    for code, description, should_fail in tests:
        if run_test(code, description, should_fail):
            print(f"✅ Тест пройден: {description}")
            passed += 1
        else:
            print(f"❌ Тест провален: {description}")

    print(f"\n=== Результат: {passed}/{len(tests)} тестов пройдено ===")


if __name__ == "__main__":
    main()
