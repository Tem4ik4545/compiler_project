from src.semantic.symbol_table import SymbolTable
from src.semantic.type_checker import check_binary_op
from src.AST.Karkas import *

class SemanticAnalyzer:
    def __init__(self):
        self.global_scope = SymbolTable()

    def analyze(self, ast):
        self.visit_program(ast, self.global_scope)

    def visit_program(self, node, scope: SymbolTable):
        for stmt in node.statements:
            self.visit_statement(stmt, scope)

    def visit_statement(self, node, scope: SymbolTable):
        if isinstance(node, list):
            for item in node:
                self.visit_statement(item, scope)
            return

        if isinstance(node, VarDeclaration):
            self.visit_var_declaration(node, scope)
        elif isinstance(node, Assignment):
            self.visit_assignment(node, scope)
        elif isinstance(node, PrintStatement):
            self.visit_expression(node.expression, scope)
        elif isinstance(node, FunctionDeclaration):
            self.visit_function_declaration(node, scope)
        elif isinstance(node, FunctionCall):
            self.visit_function_call(node, scope)
        elif isinstance(node, ReturnStatement):
            if node.value:
                actual = self.visit_expression(node.value, scope)
                expected = scope.lookup("__return_type__")
                if expected and actual != expected.type_:
                    raise Exception(f"Ошибка: return ожидает {expected.type_}, но получено {actual}")
        elif isinstance(node, Block):
            self.visit_block(node, SymbolTable(parent=scope))
        elif isinstance(node, IfStatement):
            self.visit_if_statement(node, scope)
        elif isinstance(node, WhileStatement):
            self.visit_while_statement(node, scope)
        elif isinstance(node, ForStatement):
            self.visit_for_statement(node, scope)
        elif isinstance(node, TryCatchStatement):
            self.visit_try_catch(node, scope)
        elif isinstance(node, MatchStatement):
            self.visit_match_statement(node, scope)

    def visit_block(self, node, scope: SymbolTable):
        for stmt in node.statements:
            self.visit_statement(stmt, scope)

    def visit_var_declaration(self, node: VarDeclaration, scope: SymbolTable):
        if scope.lookup_local(node.name):
            raise Exception(f"Ошибка: Переменная '{node.name}' уже объявлена")
        expr_type = self.visit_expression(node.value, scope)
        if expr_type != node.type_:
            raise Exception(f"Несовпадение типов при инициализации '{node.name}': {node.type_} ≠ {expr_type}")
        scope.define(node.name, node.type_)

    def visit_assignment(self, node: Assignment, scope: SymbolTable):
        symbol = scope.lookup(node.name)
        if not symbol:
            raise Exception(f"Переменная '{node.name}' не объявлена")
        expr_type = self.visit_expression(node.value, scope)
        if expr_type != symbol.type_:
            raise Exception(f"Несовпадение типов в присваивании '{node.name}': {symbol.type_} ≠ {expr_type}")

    def visit_function_declaration(self, node: FunctionDeclaration, scope: SymbolTable):
        if scope.lookup_local(node.name):
            raise Exception(f"Ошибка: Функция '{node.name}' уже объявлена")

        scope.define(node.name, {
            "return_type": node.return_type,
            "params": node.params
        })

        func_scope = SymbolTable(parent=scope)
        func_scope.define("__return_type__", node.return_type)  # ✅ сюда!

        seen_params = set()
        for name, type_ in node.params:
            if name in seen_params:
                raise Exception(f"Ошибка: Повторяющийся параметр '{name}' в функции '{node.name}'")
            seen_params.add(name)
            func_scope.define(name, type_)

        self.visit_block(node.body, func_scope)

    def visit_expression(self, node, scope: SymbolTable):
        if isinstance(node, list):
            result = None
            for item in node:
                result = self.visit_expression(item, scope)
            return result

        elif isinstance(node, Literal):
            if isinstance(node.value, bool):
                return "bool"
            elif isinstance(node.value, int):
                return "int"
            elif isinstance(node.value, float):
                return "float"
            elif isinstance(node.value, str):
                return "string"

        elif isinstance(node, Identifier):
            symbol = scope.lookup(node.name)
            if not symbol:
                raise Exception(f"Переменная '{node.name}' не объявлена")
            return symbol.type_

        elif isinstance(node, BinaryOp):
            left_type = self.visit_expression(node.left, scope)
            right_type = self.visit_expression(node.right, scope)
            result_type = check_binary_op(left_type, node.op, right_type)
            node.type_ = result_type  # Сохраняем тип в узле
            return result_type

        elif isinstance(node, UnaryOp):
            operand_type = self.visit_expression(node.operand, scope)
            if node.op == "!":
                if operand_type != "bool":
                    raise Exception(f"Ошибка: Оператор '!' применим только к bool, а не к {operand_type}")
                return "bool"
            else:
                raise Exception(f"Ошибка: Неизвестный унарный оператор '{node.op}'")

        elif isinstance(node, FunctionCall):
            return self.visit_function_call(node, scope)

        return None

    def visit_if_statement(self, node: IfStatement, scope: SymbolTable):
        cond_type = self.visit_expression(node.condition, scope)
        if cond_type != "bool":
            raise Exception(f"Ошибка: Условие в if должно быть типа bool, а не {cond_type}")
        self.visit_block(node.then_block, SymbolTable(parent=scope))
        if node.else_block:
            self.visit_block(node.else_block, SymbolTable(parent=scope))

    def visit_while_statement(self, node: WhileStatement, scope: SymbolTable):
        cond_type = self.visit_expression(node.condition, scope)
        if cond_type != "bool":
            raise Exception(f"Ошибка: Условие в while должно быть типа bool, а не {cond_type}")
        self.visit_block(node.body, SymbolTable(parent=scope))

    def visit_for_statement(self, node: ForStatement, scope: SymbolTable):
        for_scope = SymbolTable(parent=scope)
        if node.init:
            self.visit_statement(node.init, for_scope)
        if node.condition:
            cond_type = self.visit_expression(node.condition, for_scope)
            if cond_type != "bool":
                raise Exception(f"Ошибка: Условие в for должно быть типа bool, а не {cond_type}")
        if node.update:
            self.visit_statement(node.update, for_scope)
        self.visit_block(node.body, for_scope)

    def visit_try_catch(self, node: TryCatchStatement, scope: SymbolTable):
        self.visit_block(node.try_block, SymbolTable(parent=scope))

        if scope.lookup_local("e"):
            raise Exception("Ошибка: Переменная 'e' в catch уже объявлена")

        catch_scope = SymbolTable(parent=scope)
        catch_scope.define("e", "string")
        self.visit_block(node.catch_block, catch_scope)

    def visit_match_statement(self, node: MatchStatement, scope: SymbolTable):
        expr_type = self.visit_expression(node.expr, scope)
        for case in node.cases:
            value_type = self.visit_expression(case.value, scope)
            if value_type != expr_type:
                raise Exception(f"Тип значения case '{value_type}' не совпадает с типом match '{expr_type}'")
            self.visit_statement(case.body, SymbolTable(parent=scope))
        if node.default:
            self.visit_statement(node.default.body, SymbolTable(parent=scope))

    def visit_function_call(self, node: FunctionCall, scope: SymbolTable):
        symbol_entry = scope.lookup(node.name)
        if not symbol_entry:
            raise Exception(f"Функция '{node.name}' не объявлена")

        function_info = symbol_entry.type_

        if not isinstance(function_info, dict) or "params" not in function_info:
            raise Exception(f"Функция '{node.name}' определена некорректно")

        expected_params = function_info["params"]
        if len(node.arguments) != len(expected_params):
            raise Exception(
                f"Функция '{node.name}' ожидает {len(expected_params)} аргумента(ов), получено {len(node.arguments)}")

        for arg, (param_name, param_type) in zip(node.arguments, expected_params):
            arg_type = self.visit_expression(arg, scope)
            if arg_type != param_type:
                raise Exception(f"Тип аргумента '{param_name}' не совпадает: ожидался {param_type}, получен {arg_type}")

        return function_info["return_type"]

