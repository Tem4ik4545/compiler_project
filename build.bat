@echo off
echo [🔧] Активируем виртуальное окружение...
call .venv\Scripts\activate

echo [🚀] Шаг 1: Компиляция example.my в NASM...
python -m src.main example.my build/output.asm
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Ошибка компиляции .my → .asm
    pause
    exit /b
)

echo [🔩] Шаг 2: NASM сборка ASM → OBJ...
nasm -f win64 -o build/output.obj build/output.asm
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Ошибка NASM на этапе .asm → .obj
    pause
    exit /b
)

echo [🔗] Шаг 3: Линковка OBJ → EXE...
gcc build/output.obj -o build/output.exe -nostartfiles -Wl,--entry=_start -lkernel32 -luser32 -lmsvcrt
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Ошибка линковки .exe
    pause
    exit /b
)

echo [✅] Успешная сборка!
echo ----------------------------
echo Запуск output.exe...
build\output.exe
echo ----------------------------
pause
