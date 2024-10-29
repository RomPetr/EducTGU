import os
from tkinter import *
from tkinter import filedialog as fd
import shutil

"""
# копирование директории
window = Tk()
window.withdraw()

direct = fd.askdirectory(title="Выберите папку для копирования")

if direct:
    new_dir = direct + "_new"
    if not os.path.exists(new_dir):
        try:
            shutil.copytree(direct, new_dir)
            print(f"Все содержимое папки {direct} скопировано в папку {new_dir}")
        except Exception as e:
            print(f"Ошибка при копировании: {e}")
    else:
        print(f"Папка {new_dir} уже существует")
else:
    print("Папка не была выбрана")
"""

# копирование изображений
window = Tk()
window.withdraw()

direct = fd.askdirectory(title="Выберите папку с изображениями для их копирования")

if direct:
    new_dir = direct + "_new"
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    else:
        print(f"Папка {new_dir} уже существует")
    for file in os.listdir(direct):
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
            source_file = os.path.join(direct, file)
            destination_file = os.path.join(new_dir, file)
            try:
                shutil.move(source_file, destination_file)
                print("Файл перемещен")
            except Exception as e:
                print(f"Ошибка перемещения файла {file}: {e}")
    print("Все скопировано")
else:
    print("Папка не была выбрана")

window.mainloop()
