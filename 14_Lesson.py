from tkinter import *
import time
import datetime
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import pygame


def set_reminder():
    global r_time
    time_reminder = sd.askstring(title="Время напоминания", prompt="Введите время в формате ЧЧ:ММ")
    if time_reminder:
        try:
            hour, minute = time_reminder.split(":")
            hour = int(hour)
            minute = int(minute)
            now_time = datetime.datetime.now()
            print(now_time)
            r_time = now_time.replace(hour=hour, minute=minute, second=0)
            print(r_time)
            r_time = r_time.timestamp()
            mb.showinfo(title="Успех", message=f"Напоминание установлено на {hour}:{minute}")
            check_time()
        except ValueError:
            mb.showerror("Ошибка", f"Неправильно указано время")


def check_time():
    global r_time
    if r_time:
        now = time.time()
        print(f"Текущее время - {now}")
        print(f"Напоминание - {r_time}")
        if now >= r_time:
            # print("Играет музыка")
            play_music()
            r_time = 0
        window.after(5000, check_time)


def play_music():
    global music
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()
    music = True


def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False


music = False
r_time = 0

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

window.mainloop()
