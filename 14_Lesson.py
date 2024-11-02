from tkinter import *
import datetime
import time
from time import strftime
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import pygame

text_rem = ''  # Global variable for reminder text
music = False
now_time = 0
r_time = 0


def set_reminder():
    global r_time, now_time, text_rem
    time_reminder = sd.askstring(title="Время напоминания", prompt="Введите время в формате ЧЧ:ММ")
    if time_reminder:
        try:
            hour, minute = time_reminder.split(":")
            hour = int(hour)
            minute = int(minute)
            now_time = datetime.datetime.now()
            # print(now_time)
            r_time = now_time.replace(hour=hour, minute=minute, second=0)
            # print(r_time)
            r_time = r_time.timestamp()

            # в следующей строке предлагается ввести текст напоминания
            text_rem = sd.askstring("Текст напоминания", "Введите текст напоминания.")
            mb.showinfo(title="Успех", message=f"Напоминание установлено на {hour}:{minute}")
            check_time() # запуск отслеживания времени срабатывания напоминания
        except ValueError:
            mb.showerror("Ошибка", f"Неправильно указано время")


def check_time():
    global now_time, r_time
    if r_time:
        now = time.time()
        # print(f"Текущее время - {now}") для отладки
        # print(f"Напоминание - {r_time}") для отладки
        # now_time = datetime.datetime.now()
        # bottom_label.config(text=str(now_time.strftime('%H:%M')))
        if now >= r_time:
            # print("Играет музыка") для отладки
            play_music()
            r_time = 0
        window.after(3000, check_time)


def play_music():
    global music
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()
    music = True
    show_reminder() # вызов функции отображения напоминания


def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    lab.config(text="Установить новое напоминание")


def show_reminder():
    global text_rem
    mb.showinfo(title="Напоминание", message=text_rem)


def lab_time():
    current_time = strftime('%H:%M:%S')
    bottom_label.config(text=current_time)
    bottom_label.after(1000, lab_time)  # обновление каждые 1000 миллисекунд (1 секунда)


window = Tk()
window.title("Напоминалка")
width_d = window.winfo_screenmmwidth()
height_d = window.winfo_screenheight()
# print(width_d, height_d)
window.geometry(f"300x200+{width_d//2-150}+{height_d//2-100}")

lab = Label(window, text="--Нажмите на кнопку и установите\n напоминание на любое время--")
lab.pack(pady=5)

btn = Button(window, text="Установить напоминание", command=set_reminder)
btn.pack(pady=5)

btn_stop_music = Button(window, text="Остановить музыку", command=stop_music)
btn_stop_music.pack(pady=5)

# --- блок отображения текущего времени
bottom_label = Label(window, text='time', font=('calibri', 12, 'bold'))
bottom_label.pack(pady=20, anchor='center')

lab_time()
# ---

window.mainloop()
