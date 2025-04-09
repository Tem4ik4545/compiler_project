def check_binary_op(left_type: str, op: str, right_type: str):
    arithmetic_ops = {"+", "-", "*", "/"}
    comparison_ops = {"<", ">", "==", "!="}
    logical_ops = {"&&", "||"}
    if op in arithmetic_ops:
        if left_type in ("int", "float") and right_type in ("int", "float"):
            if left_type == "float" or right_type == "float":
                return "float"
            return "int"
        else:
            raise Exception(f"Ошибка: Неверные типы для арифметической операции: {left_type} {op} {right_type}")
    elif op in comparison_ops:
        if left_type == right_type:
            return "bool"
        else:
            raise Exception(f"Ошибка: Типы для сравнения не совпадают: {left_type} {op} {right_type}")
    elif op in logical_ops:
        if left_type == "bool" and right_type == "bool":
            return "bool"
        else:
            raise Exception(f"Ошибка: Неверные типы для логической операции: {left_type} {op} {right_type}")
    else:
        raise Exception(f"Ошибка: Неизвестный оператор '{op}'")
