from src.IR.ir_generator import IRGenerator
from src.IR.ir_optimizer import IROptimizer
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
    code = '''
    {
        let x: int = 5;
        let y: int = 10;
        let z: int = x + y;
        print(z);
    }
    '''
    run_nasm_test(code, "Простой арифметический пример")

if __name__ == "__main__":
    main()