import os
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import shutil
from datetime import datetime

# сортировка изображений по папкам

def choose_dir():
    direct = fd.askdirectory()
    if direct:
        organize_photos(direct)


def organize_photos(directory):
    for file in os.listdir(directory):
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
            filepath = os.path.join(directory, file)
            timestamp = os.path.getctime(filepath) # возвращает в переменную дату и время создания файла
            date = datetime.fromtimestamp(timestamp)
            year_month = date.strftime("%Y_%m")
            new_dir = os.path.join(directory, year_month)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            shutil.move(filepath, os.path.join(new_dir, file))
    mb.showinfo("Готово!", "Все фотографии рассортированы")

window = Tk()
window.withdraw()

choose_dir()

window.mainloop()