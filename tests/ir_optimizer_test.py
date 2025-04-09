from src.IR.instructions import *
from src.IR.ir_optimizer import IROptimizer

def run_optimization_test(name, original_ir, expected_ir):
    print(f"\n=== Тест оптимизации IR: {name} ===")

    optimizer = IROptimizer()
    optimized = optimizer.optimize(original_ir)

    optimized_str = "\n".join(str(instr) for instr in optimized)
    expected_str = "\n".join(str(instr) for instr in expected_ir)

    print("\n--- Оптимизированный IR ---")
    print(optimized_str)

    print("\n--- Эталонный IR ---")
    print(expected_str)

    if optimized_str.strip() == expected_str.strip():
        print("\n✅ Оптимизация прошла успешно и соответствует ожиданиям.")
    else:
        print("\n❌ Результат оптимизации не совпадает с эталоном.")

def main():
    # 1. Свертка констант
    run_optimization_test("Свертка констант", [
        IRBinary("t1", 2, "+", 3),
        IRPrint("t1")
    ], [
        IRAssign("t1", 5),
        IRPrint("t1")
    ])

    # 2. Пропагация копий
    run_optimization_test("Пропагация копий", [
        IRAssign("t1", "x"),
        IRAssign("t2", "t1"),
        IRPrint("t2")
    ], [
        IRPrint("x")  # ✅ исправлено
    ])

    # 3. Удаление неиспользуемых временных
    run_optimization_test("Удаление неиспользуемых временных", [
        IRAssign("t1", 42),
        IRAssign("x", 1),
        IRPrint(1)
    ], [
        IRPrint(1)
    ])

    # 4. Бесполезное присваивание
    run_optimization_test("Бесполезное присваивание", [
        IRAssign("x", "x"),
        IRAssign("x", 5)
    ], [
        # ничего не осталось, т.к. x не используется
    ])

    # 5. Упрощение if с true
    run_optimization_test("Упрощение if с true", [
        IRIfGoto("true", "label1"),
        IRGoto("label2")
    ], [
        IRGoto("label1"),
        IRGoto("label2")
    ])

    # 6. Удаление мертвого кода после return
    run_optimization_test("Удаление мертвого кода после return", [
        IRReturn("x"),
        IRAssign("y", 5)
    ], [
        IRReturn("x")
    ])

    # 7. Удаление бесполезных call
    run_optimization_test("Удаление бесполезных call", [
        IRCall("tmp", "foo", []),
        IRPrint("x")
    ], [
        IRCall("tmp", "foo", []),
        IRPrint("x")
    ])

    # 8. Удаление лишнего tmp при арифметике
    run_optimization_test("Удаление лишнего tmp при арифметике", [
        IRBinary("t1", 3, "*", 2),
        IRAssign("x", "t1")
    ], [
        # x не используется → всё удалено
    ])


if __name__ == "__main__":
    main()
