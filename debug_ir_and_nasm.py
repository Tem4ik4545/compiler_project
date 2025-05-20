import sys
from antlr4 import FileStream, CommonTokenStream

from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser
from src.AST.ASTBuilder import ASTBuilder
from src.semantic.semantic_analyzer import SemanticAnalyzer
from src.IR.ir_generator import IRGenerator
from src.optimizer.ir_optimizer import IROptimizer
from src.Nasm.nasm_generator import NASMGenerator

def debug_compile(source_file: str):
    print(f"🔍 Анализ файла: {source_file}\n")

    # 1. Лексер и парсер
    input_stream = FileStream(source_file, encoding="utf-8")
    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyLangParser(token_stream)
    tree = parser.program()

    # 2. Построение AST
    print("=== 🧱 AST ===")
    ast = ASTBuilder().visit(tree)
    print(ast)
    print()

    # 3. Семантический анализ
    print("=== ✅ Semantic ===")
    SemanticAnalyzer().analyze(ast)
    print("Semantic OK\n")

    # 4. IR до оптимизации
    ir = IRGenerator().generate(ast)
    print("=== 🧾 IR до оптимизации ===")
    for instr in ir:
        print(instr)
    print()



    # 6. NASM
    print("=== ⚙️ NASM-код ===")
    nasm_code = NASMGenerator().generate(ir)
    print(nasm_code)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ Использование: python debug_ir_and_nasm.py <входной_файл.my>")
        sys.exit(1)

    debug_compile(sys.argv[1])
