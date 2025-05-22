from src.IR.temp_manager import TempManager
from src.IR.instructions import *
from src.semantic.symbol_table import SymbolTable
from src.AST.Karkas import Literal, Identifier, BinaryOp

class IRGenerator:
    def __init__(self):
        self.temp = TempManager()
        self.instructions = []
        self.defined_funcs = set()
        self.generated_labels = set()
        self.current_scope = SymbolTable()

    def generate(self, node):
        self.instructions = []
        self.temp = TempManager()
        self.defined_funcs = set()
        self.generated_labels = set()
        self.visit(node)
        return self.instructions

    def visit(self, node):
        if isinstance(node, list):
            for item in node:
                self.visit(item)
            return
        method = f"visit_{type(node).__name__}"
        return getattr(self, method, self.generic_visit)(node)

    def generic_visit(self, node):
        raise Exception(f"No visit method for {type(node).__name__}")

    def visit_Program(self, node):
        for stmt in node.statements:
            if stmt is not None:
                self.visit(stmt)

    def visit_VarDeclaration(self, node):
        value = self.visit(node.value)
        self.current_scope.define(node.name, node.type_)
        if isinstance(value, (IRCall, IRBinary, IRUnary)):
            self.instructions.append(IRAssign(node.name, value.result, type_=node.type_))
        else:
            self.instructions.append(IRAssign(node.name, value, type_=node.type_))



    def visit_Assignment(self, node):
        value = self.visit(node.value)
        self.instructions.append(IRAssign(node.name, value))

    def visit_expression(self, node):
        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return "string"
            elif isinstance(node.value, int):
                return "int"
            elif isinstance(node.value, float):
                return "float"
            elif isinstance(node.value, bool):
                return "bool"
        elif isinstance(node, Identifier):
            symbol = self.current_scope.lookup(node.name)
            if symbol:
                return symbol.type_
        elif isinstance(node, BinaryOp):
            return node.type_

        return "int"

    def visit_PrintStatement(self, node):
        expr_type = self.visit_expression(node.expression)
        value = self.visit(node.expression)
        self.instructions.append(IRPrint(value, expr_type))

    def visit_ReturnStatement(self, node):
        if node.value is None:
            self.instructions.append(IRReturn(None))
            return

        if isinstance(node.value, (IRBinary, IRUnary, IRCall)):
            # временно сохраним текущие инструкции
            old_instructions = self.instructions
            self.instructions = []
            val = self.visit(node.value)
            instrs = self.instructions
            self.instructions = old_instructions
            self.instructions.extend(instrs)
            self.instructions.append(IRReturn(val))
        else:
            value = self.visit(node.value)
            self.instructions.append(IRReturn(value))

    def visit_IfStatement(self, node):
        else_label = self._unique_label("else")
        end_label = self._unique_label("endif")

        cond = self.visit(node.condition)

        negated = self.temp.new_temp()
        self.instructions.append(IRUnary(negated, "!", cond))

        self.instructions.append(IRIfGoto(negated, else_label))
        self.visit(node.then_block)
        self.instructions.append(IRGoto(end_label))
        self.instructions.append(IRLabel(else_label))
        if node.else_block:
            self.visit(node.else_block)
        self.instructions.append(IRLabel(end_label))

    def visit_WhileStatement(self, node):
        start_label = self._unique_label("while_start")
        end_label = self._unique_label("while_end")
        self.instructions.append(IRLabel(start_label))
        condition = self.visit(node.condition)
        self.instructions.append(IRIfGoto(f"!{condition}", end_label))
        self.visit(node.body)
        self.instructions.append(IRGoto(start_label))
        self.instructions.append(IRLabel(end_label))

    def visit_ForStatement(self, node):
        self.visit(node.init)
        start_label = self._unique_label("for_start")
        end_label = self._unique_label("for_end")
        self.instructions.append(IRLabel(start_label))
        condition = self.visit(node.condition)
        self.instructions.append(IRIfGoto(f"!{condition}", end_label))
        self.visit(node.body)
        self.visit(node.update)
        self.instructions.append(IRGoto(start_label))
        self.instructions.append(IRLabel(end_label))

    def visit_FunctionDeclaration(self, node):
        # Создаём новую область видимости для функции
        func_scope = SymbolTable(parent=self.current_scope)
        self.current_scope = func_scope  # Обновляем текущую область

        func_name = f"func_{node.name}"
        if func_name in self.defined_funcs:
            return

        # Добавляем параметры функции в область видимости
        for param_name, param_type in node.params:
            func_scope.define(param_name, param_type)

        self.defined_funcs.add(func_name)
        self.instructions.append(IRFunctionStart(func_name, [name for name, _ in node.params]))
        self.visit(node.body)
        self.instructions.append(IRFunctionEnd(func_name))

        # Возвращаемся к родительской области видимости
        self.current_scope = func_scope.parent

    def visit_FunctionCall(self, node):
        args = []
        for arg in node.arguments:
            val = self.visit(arg)
            # если это вызов, уже IRCall, то будет обработан до
            args.append(val)
        result = self.temp.new_temp()
        self.instructions.append(IRCall(result, f"func_{node.name}", args))
        return result

    def visit_BinaryOp(self, node):
        # Обрабатываем левый и правый аргументы
        left = self.visit(node.left)
        right = self.visit(node.right)

        # если результат вложенной функции — не переменная, сохранить в temp
        if isinstance(node.left, IRCall):
            tmp_left = self.temp.new_temp()
            self.instructions.append(IRAssign(tmp_left, left))
            left = tmp_left

        if isinstance(node.right, IRCall):
            tmp_right = self.temp.new_temp()
            self.instructions.append(IRAssign(tmp_right, right))
            right = tmp_right

        result = self.temp.new_temp()
        self.instructions.append(IRBinary(result, left, node.op, right, type_=node.type_))  # Передаём тип
        return result

    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        result = self.temp.new_temp()
        self.instructions.append(IRUnary(result, node.op, operand))
        return result

    def visit_Identifier(self, node):
        if not self.current_scope:
            raise Exception("Ошибка: Область видимости не инициализирована")

        # Ищем переменную в текущей области и родительских
        symbol = self.current_scope.lookup(node.name)
        if not symbol:
            raise Exception(f"Ошибка: Переменная '{node.name}' не объявлена")

        # Аннотируем узел типом из таблицы символов
        node.type_ = symbol.type_
        return node.name

    def visit_Literal(self, node):
        if isinstance(node.value, float):
            node.type_ = "float"
        elif isinstance(node.value, int):
            node.type_ = "int"
        elif isinstance(node.value, str):
            return f'"{node.value}"'
        return str(node.value)

    def visit_Block(self, node):
        for stmt in node.statements:
            if stmt is not None:
                self.visit(stmt)

    def visit_TryCatchStatement(self, node):
        try_label = self._unique_label("try")
        catch_label = self._unique_label("catch")
        end_label = self._unique_label("end_try")
        self.instructions.append(IRLabel(try_label))
        self.visit(node.try_block)
        self.instructions.append(IRGoto(end_label))
        self.instructions.append(IRLabel(catch_label))
        self.visit(node.catch_block)
        self.instructions.append(IRLabel(end_label))

    def visit_MatchStatement(self, node):
        expr_temp = self.visit(node.expr)
        end_label = self._unique_label("end_match")
        case_labels = []

        for i, case in enumerate(node.cases):
            label = self._unique_label(f"case_{i}")
            case_labels.append((label, case))
            cond = self.temp.new_temp()
            self.instructions.append(IRBinary(cond, expr_temp, "==", self.visit(case.value)))
            self.instructions.append(IRIfGoto(cond, label))

        default_label = self._unique_label("default_case") if node.default else end_label
        self.instructions.append(IRGoto(default_label))

        for label, case in case_labels:
            self.instructions.append(IRLabel(label))
            for stmt in case.body:
                self.visit(stmt)
            self.instructions.append(IRGoto(end_label))

        if node.default:
            self.instructions.append(IRLabel(default_label))
            for stmt in node.default.body:
                self.visit(stmt)

        self.instructions.append(IRLabel(end_label))

    def _unique_label(self, prefix: str) -> str:
        label = self.temp.new_label(prefix)
        while label in self.generated_labels:
            label = self.temp.new_label(prefix)
        self.generated_labels.add(label)
        return label
