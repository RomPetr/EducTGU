# работа с файлами и папками
import os
from datetime import datetime
from tkinter import *
from tkinter import filedialog as fd
'''
filepath = "/home/rp/PycharmProjects/EducTGU/111.txt"
last_modified_time = os.path.getatime(filepath)
print("Время последнего изменения: ", last_modified_time)
ft = datetime.fromtimestamp(last_modified_time).strftime("%Y-%m-%d  %H:%M:%S")
print("Дата и время изменения: ", ft)
'''

# вывод в консоль список файлов и папок выбранной директории с временными метками
window = Tk()
window.withdraw()

direct = fd.askdirectory()

if direct:
    for file in os.listdir(direct):
        if file.lower().endswith(('.jpg', '.jpeg', '.bmp', '.png')):
            filepath = os.path.join(direct, file) # объединили путь и файл
            lt = os.path.getmtime(filepath)
            ft = datetime.fromtimestamp(lt).strftime("%d.%m.%Y  %H:%M:%S")
            print(f"Файл: {file} Дата и время модификации: {ft}")

window.mainloop()