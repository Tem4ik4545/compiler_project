import sys
from antlr4.error.ErrorListener import ConsoleErrorListener

from antlr4 import *
from src.lexer.MyLangLexer import MyLangLexer
from src.parser.MyLangParser import MyLangParser


def format_tree(tree, parser, indent=0):
    """Форматирует дерево разбора с отступами"""
    if tree.getChildCount() == 0:
        return "  " * indent + tree.getText()

    rule_name = parser.ruleNames[tree.getRuleIndex()] if hasattr(tree, 'getRuleIndex') else str(tree)
    result = "  " * indent + rule_name + "\n"

    for i in range(tree.getChildCount()):
        result += format_tree(tree.getChild(i), parser, indent + 1) + "\n"

    return result.strip()


def parse_code(code: str):
    input_stream = InputStream(code)

    lexer = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # 📌 Лексический анализ
    lexer.reset()
    token_stream.fill()  # Загружаем все токены
    print("\n🎯 Токены, распознанные лексером:")
    for token in token_stream.tokens:
        print(f"Токен: {lexer.symbolicNames[token.type]} = '{token.text}' "
              f"(строка {token.line}, позиция {token.column})")

    parser = MyLangParser(token_stream)

    # 📌 Обработчик ошибок парсера
    parser.removeErrorListeners()
    parser.addErrorListener(ConsoleErrorListener.INSTANCE)

    # 📌 Синтаксический анализ
    #print("\n🔍 Токены перед разбором парсером:")
    #for token in token_stream.tokens:
        #print(f"Токен: {lexer.symbolicNames[token.type]} = '{token.text}' "
              #f"(строка {token.line}, позиция {token.column})")

    tree = parser.program()

    # 📌 Вывод отформатированного дерева разбора
    print("\n🌳 Дерево разбора (форматированное):")
    print(format_tree(tree, parser))


# ✅ Тестовый код, который проверяет все конструкции языка
code = """
{
    
    let x: int = 5;
    let y: bool = true;
    let name: string = "Hello";
    let pi: float = 3.14;
    let radius: float = 2.5;
    let area: float = pi * radius * radius;
    print(area);
    
    print(x);
    print(name);

    
    if (x > 3) { print("x больше 3"); }
    else { print("x меньше или равен 3"); }

    
    for (let i: int = 0; i < 5; i = i + 1) { 
    for (let j: int = 0; j < 5; j= j +1) { print(j);}
    print(i);}
    for (;;) { print("Бесконечный цикл"); }

    
    while (x > 0) {
        print(x);
        x = x - 1;
    }

    
    function square(n: int): int {
        return n * n;
    }
    let result: int = square(4);
    print(result);
    
    

    
    
    try {
        let z: int = 5 / 0;
    } catch (e) {
        print("Ошибка деления на ноль");
    }

    
    match x {
        case 1: print("Один");
        case 5: print("Пять");
        default: print("Другое число");
    }
}
"""

parse_code(code)
