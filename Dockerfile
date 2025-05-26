FROM python:3.11-slim

# Установка утилит: nasm, gcc и MinGW для сборки .exe
RUN apt update && apt install -y nasm gcc mingw-w64

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем всё из проекта в контейнер
COPY . /app

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Делаем скрипт сборки исполняемым
RUN chmod +x build_inside.sh

# Точка входа — сборочный скрипт
ENTRYPOINT ["bash", "build_inside.sh"]
