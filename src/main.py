import sys
from antlr4 import FileStream, CommonTokenStream
from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser
from src.AST.ASTBuilder import ASTBuilder
from src.semantic.semantic_analyzer import SemanticAnalyzer
from src.IR.ir_generator import IRGenerator
from src.optimizer.ir_optimizer import IROptimizer
from src.Nasm.nasm_generator import NASMGenerator
import os


def compile_source(source_file: str, output_file: str):
    print(f"🔧 Компиляция файла: {source_file}")

    # 1. Лексер и парсер
    input_stream = FileStream(source_file, encoding="utf-8")
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)
    tree = parser.program()

    # 2. Построение AST
    ast = ASTBuilder().visit(tree)
    print("✅ AST построено")

    # 3. Семантический анализ
    SemanticAnalyzer().analyze(ast)
    print("✅ Семантический анализ пройден")

    # 4. Генерация IR
    ir = IRGenerator().generate(ast)
    print("✅ IR сгенерирован")

    # 5. Оптимизация IR
    optimized_ir = IROptimizer().optimize(ir)
    print("✅ IR оптимизирован")

    # 6. Генерация NASM
    nasm_code = NASMGenerator().generate(optimized_ir)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(nasm_code)
    print(f"✅ NASM-код сохранён в {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("❗ Использование: python main.py <входной_файл.my> <выходной_файл.asm>")
        sys.exit(1)

    source_path = sys.argv[1]
    output_path = sys.argv[2]
    compile_source(source_path, output_path)
