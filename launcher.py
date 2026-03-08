import importlib
import sys
import re
import lexicon
import time
importlib.reload(lexicon)

def run_yashcher(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
        контекст = {
        "очистить_экран":
очистить_экран
        }
    for russian, python in lexicon.data.items():
        pattern = r'\b' + re.escape(russian) + r'\b'
        code = re.sub(pattern, python, code)
    try:
        exec(code, контекст)
    except Exception as e:
        print("\n--- ОШИБКА ЯЩЕРА ---")
        print("Кажется, в коде есть баг.")
        print(f"Детали: {e}")
        print("Проверь синтаксис и попробуй снова.")

def очистить_экран():
    print("\n" * 150, " ")

if __name__ == "__main__":
    print("-" * 14, "ДОБРО ПОЖАЛОВАТЬ В 'ЯЩЕР V1.0'!", "-" * 14)
    print("Введите имя файла, формата .ЯЩЕР, например тест.ящер, писать формат .ящер здесь необязательно! ")
    file_name = input("Имя файла: ")
    if not file_name.endswith(".ящер"):
        file_name += ".ящер"
    run_yashcher(file_name)