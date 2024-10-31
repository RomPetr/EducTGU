from tkinter import *
import time
import datetime
from tkinter import simpledialog as sd
from tkinter import messagebox as mb

def set_reminder():
    time_reminder = sd.askstring(title="Время напоминания", prompt="Введите время в формате ЧЧ:ММ")
    if time_reminder:
        try:
            hour, minute = time_reminder.split(":")
            hour = int(hour)
            minute = int(minute)
            now_time = datetime.datetime.now()
            print(now_time)
            time_r = now_time.replace(hour=hour, minute=minute)
            print(time_r)
            mb.showinfo(title="Успех", message=f"Напоминание установлено на {hour}:{minute}")
        except ValueError:
            mb.showerror("Ошибка", f"Неправильно указано время")


window = Tk()
window.title("Напоминалка")
width_d = window.winfo_screenmmwidth()
height_d = window.winfo_screenheight()
print(width_d, height_d)
window.geometry(f"300x200+{width_d//2-150}+{height_d//2-100}")

l = Label(window, text="--Нажмите на кнопку и установите\n напоминание на любое время--")
l.pack(pady=5)

btn = Button(window, text="Установить напоминание", command=set_reminder)
btn.pack(pady=5)


window.mainloop()