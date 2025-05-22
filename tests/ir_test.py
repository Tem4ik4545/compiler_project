from antlr4 import *
from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser
from src.AST.ASTBuilder import ASTBuilder
from src.IR.ir_generator import IRGenerator
from src.semantic.semantic_analyzer import SemanticAnalyzer
from src.optimizer.ir_optimizer import IROptimizer
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

    SemanticAnalyzer().analyze(ast)
    print("✅ Семантический анализ пройден")


    ir_gen = IRGenerator()
    ir = ir_gen.generate(ast)

    optimized_ir = IROptimizer().optimize(ir)
    print("\n--- Сгенерированный оптимизорованный трёхадресный код (IR) ---")
    for instr in optimized_ir:
        print(instr)



def main():
    code = r'''
    {
        let k: int = 2;
        let m: float = 3.1415926;
        let v: float = m + 1.2;
        print(v);
        print(k);
        
    }
    '''

    run_ir_test(code, "Полный тест конструкций")


if __name__ == "__main__":
    main()
