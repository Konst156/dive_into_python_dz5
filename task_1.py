# ✔Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os


def split_path(file_path):
    path, filename = os.path.split(file_path)
    filename, extension = os.path.splitext(filename)
    return path, filename, extension


file_path = r"C:\Users\kzhes\OneDrive\Рабочий стол\Программирование\GB\Погружение в Python\venv\Scripts\python.exe"
result = split_path(file_path)
print(result)
