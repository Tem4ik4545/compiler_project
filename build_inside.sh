#!/bin/bash
set -e

echo "[1] Компиляция .my → .asm"
python -m src.main example.my build/output.asm

echo "[2] Ассемблирование .asm → .obj"
nasm -f win64 -o build/output.obj build/output.asm

echo "[3] Линковка .obj → .exe"
x86_64-w64-mingw32-gcc build/output.obj -o build/output.exe -lkernel32 -lmsvcrt

echo "[✅] Готово: build/output.exe"