from tkinter import *
from tkinter import messagebox as mb
import random

"""
def check():
    answer = mb.askyesno(title="Вопрос", message="Передать данные?")
    if answer:
        s = e.get()
        e.delete(0, END)
        m['text'] = s

window = Tk()
e = Entry()
e.pack()
b= Button(text="передать?", command=check)
b.pack()
m = Label(height=3)
m.pack()

window.mainloop()
"""

# Игра угадай число
def check():
        s = e.get()
        s = int(s)
        rnd = random.randint(1,6)
        if s == rnd:
            mb.showinfo(title='Результат', message='Угадал!')
        else:
            mb.showinfo(title='Результат', message='Неудача...')
        answer = mb.askretrycancel(title='Вопрос', message='Загадать еще?')
        if answer:
            e.delete(0, END)
        else:
            window.destroy()

window = Tk()
window.title("Игра 'угадай число'")
m1 = Label(text='Введи число и нажми на кнопку')
e = Entry()
e.pack()
b= Button(text="Угадать", command=check)
b.pack()
m = Label(width=40, height=3)
m.pack()

window.mainloop()