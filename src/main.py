import sys
from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser
from src.IR.ir_generator import IRGenerator
from src.codegen.codegen import CodeGenerator


def main():
    if len(sys.argv) < 2:
        print("Usage: python lexerANDparser-test.py <source_file>")
        return

    source_file = sys.argv[1]

    # Читаем исходный код
    with open(source_file, 'r', encoding='utf-8') as f:
        source_code = f.read()

    # Лексический анализ
    lexer = MyLangLexer(source_code)
    tokens = lexer.tokenize()

    # Синтаксический анализ
    parser = MyLangParser(tokens)
    syntax_tree = parser.parse()

    # Генерация IR
    ir_generator = IRGenerator(syntax_tree)
    ir_code = ir_generator.generate()

    # Генерация машинного кода
    codegen = CodeGenerator(ir_code)
    compiled_code = codegen.compile()

    print("Compilation successful!")
    print(compiled_code)


if __name__ == "__main__":
    main()
