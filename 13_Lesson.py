import os
from tkinter import filedialog as fd
from datetime import datetime
import shutil

"""
# создаем папки с годами от 2020 до 2024
try:
    year = 2020
    for i in range(5):
        os.mkdir(f"{year}_год")
        year += 1
except FileExistsError:
    print("Папка уже существует")
"""

# склеивание путь до папки с файлом в полный путь
# filepath = os.path.join(dir, file)

"""
dir = fd.askdirectory()
if dir:
    for num, i in enumerate(os.listdir(dir)):
        if i.endswith(".txt"):
            filepath = os.path.join(dir, i)
            time = os.path.getmtime(filepath)
            # print(f"{i} Время изменения: {time}")
            normal_time = datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
            print(f"{num+1}. Файл: {i} Дата и время изменения: {normal_time}")
        else:
            print(f"{num+1}. Файл: {i} не в формате 'txt'")
"""

"""
# копирование файлов
dir = fd.askdirectory(title="Выбор директории")
if dir:
    name_new_dir = dir + "_new"
    print(dir)
    print(name_new_dir)
    # if not os.path.exists(name_new_dir):
    #     os.makedirs(name_new_dir)
    # else:
    #     print(f"{name_new_dir} уже существует")
    shutil.copytree(dir, name_new_dir)
    # for i in os.listdir(dir):
    #     if i.lower().endswith(('.jpg', '.png', '.bmp', '.mp4')):
    #         filepath = os.path.join(dir, i)
    #         shutil.copytree(filepath, name_new_dir)
"""
text = "abcdefg"
print(text[::2])
