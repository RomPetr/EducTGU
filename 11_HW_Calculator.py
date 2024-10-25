from tkinter import *
from tkinter import messagebox as mb

def add():
    n1 = num1.get()
    if not n1.lstrip('-').isdigit():
        mb.showerror(title="Ошибка", message="В первое поле вводите только целое число")
        return
    n2 = num2.get()
    if not n2.lstrip('-').isdigit():
        mb.showerror(title="Ошибка", message="Во второе поле вводите только целое число")
        return
    n3 = num3.get()
    if not n3.lstrip('-').isdigit():
        mb.showerror(title="Ошибка", message="В третье поле вводите только целое число")
        return

    rez_add = int(n1) + int(n2) + int(n3)
    t_rez.config(text=f"{n1} + {n2} + {n3} = {rez_add}")

    answer = mb.askretrycancel(title="Вопрос", message="Произвести еще одну операцию?")
    if answer:
        num1.delete(0, END)
        num2.delete(0, END)
        num3.delete(0, END)
        t_rez['text'] = ""
    else:
        window.destroy()

def multiply():
    n1 = num1.get()
    if not n1.lstrip('-').isdigit():
        mb.showerror(title="Ошибка", message="В первое поле вводите только целое число")
        return
    n2 = num2.get()
    if not n2.lstrip('-').isdigit():
        mb.showerror(title="Ошибка", message="Во второе поле вводите только целое число")
        return
    n3 = num3.get()
    if not n3.lstrip('-').isdigit():
        mb.showerror(title="Ошибка", message="В третье поле вводите только целое число")
        return

    rez_mul = int(n1) * int(n2) * int(n3)
    t_rez.config(text=f"{n1} * {n2} * {n3} = {rez_mul}")

    answer = mb.askretrycancel(title="Вопрос", message="Произвести еще одну операцию?")
    if answer:
        num1.delete(0, END)
        num2.delete(0, END)
        num3.delete(0, END)
        t_rez['text'] = ""
    else:
        window.destroy()

#------------------------------------------------
window = Tk()
window.title("Калькулятор")

t_top = Label(window, text=" Введите три числа и нажмите на кнопку арифметической операции", font=('MS Sans Serif', 10)).pack()

t_m1 = Label(window, text="Введите первое число:", font=("Arial", 14)).pack()
num1 = Entry(window, font=("Arial", 16))
num1.pack()

t_m2 = Label(window, text="Введите второе число:", font=("Arial", 14)).pack()
num2 = Entry(window, font=("Arial", 16))
num2.pack()

t_m3 = Label(window, text="Введите третье число:", font=("Arial", 14)).pack()
num3 = Entry(window, font=("Arial", 16))
num3.pack()

btn_add = Button(window, text="Сложить три числа", command=add)
btn_add.pack()

btn_mul = Button(window, text="Умножить три числа", command=multiply)
btn_mul.pack()

t_rez = Label(window, text="", font=("MS Sans Serif", 14))
t_rez.pack(ipady=20)

window.mainloop()