from tkinter import *
from tkinter import messagebox as mb
import random

"""
def get_info():
    answer = mb.askokcancel(title="Подтверждение", message="Получить данные с поля Entry?")
    if answer:
        content = e.get()
        e.delete(0, END)
        t_m.config(text=content)

window = Tk()
window.title("MessageBox")
window.geometry("400x300+100+200")

e = Entry(window, font=('Arial', 18))
e.pack()
btn = Button(window, text="Получить", font=('Arial', 18), command=get_info)
btn.pack()
t_m = Label(window, font=('Arial', 18))
t_m.pack()

window.mainloop()
"""

"""
# угадай число

def check_number():
    num = e.get()
    r_num = random.randint(1, 3)
    if int(num) == r_num:
        mb.showinfo(title="Результат", message="Вы угадали число")
    else:
        mb.showinfo(title="Результат", message=f"Вы не угадали число - {r_num}")
    answer = mb.askretrycancel(title="Вопрос", message="Хотите отгадать еще число?")
    if answer:
        e.delete(0, END)
    else:
        window.destroy()

window = Tk()
window.title("Угадай число")
window.geometry("400x300+100+200")

t = Label(window, text="Угадайте число:", font=('Arial', 18)).pack()
e = Entry(window, font=('Arial', 18))
e.pack()
btn = Button(window, text="Угадать", font=('Arial', 18), command=check_number)
btn.pack()
t_m = Label(window, font=('Arial', 18))
t_m.pack()

window.mainloop()
"""

"""
# Калькулятор

def add():
    number_1 = num1.get()
    number_2 = num2.get()
    if number_1 and number_2:
        if not number_1.lstrip('-').isdigit():
            mb.showerror(title="Ошибка", message="В первое поле введено не число")
            return
        if not number_2.lstrip('-').isdigit():
            mb.showerror(title="Ошибка", message="Во второе поле введено не число")
            return
        n_1 = int(number_1)
        n_2 = int(number_2)
        rez.config(text=f"{n_1} + {n_2} = {n_1 + n_2}")
    else:
        mb.showerror(title="Ошибка", message="Одно или несколько полей не заполнены")


window = Tk()
t_m1 = Label(window, text="Введите первое число:", font=("Arial", 14)).pack()
num1 = Entry(window)
num1.pack()

t_m2 = Label(window, text="Введите второе число:", font=("Arial", 14)).pack()
num2 = Entry(window)
num2.pack()

btn_add = Button(window, text="Сложение", font=("Arial", 14), command=add)
btn_add.pack()

rez = Label(window, font=("Arial", 14))
rez.pack()
window.mainloop()
"""

