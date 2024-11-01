from tkinter import *
from tkinter import ttk
import calculator_logic as c


def rezult_calc():
    res = None
    second_number = float(line_input.get())
    line_input.delete(0, END)
    if operator == "+":
        res = c.add(first_num, second_number)
    elif operator == '-':
        res = c.subtruct(first_num, second_number)
    elif operator == '*':
        res = c.multiply(first_num, second_number)
    elif operator == '/':
        res = c.divide(first_num, second_number)
    line_input.insert(0, res)

def choice_number(num):
    line_input.insert(END, num)


def choice_operator(oper):
    global operator, first_num
    first_num = float(line_input.get())
    operator = oper
    line_input.delete(0, END)

def clear_line():
    line_input.delete(0, END)

first_num = None
operator = None

window = Tk()
window.title("Калькулятор")
# window.wm_iconbitmap(bitmap="calculator_icon.ico")
line_input = Entry(window, font=('Arial', 12))
line_input.grid(row=0, column=0, columnspan=4, sticky='ew')

ttk.Button(window, text='1', command=lambda: choice_number('1')).grid(row=1, column=0)
ttk.Button(window, text='2', command=lambda: choice_number('2')).grid(row=1, column=1)
ttk.Button(window, text='3', command=lambda: choice_number('3')).grid(row=1, column=2)
ttk.Button(window, text='4', command=lambda: choice_number('4')).grid(row=2, column=0)
ttk.Button(window, text='5', command=lambda: choice_number('5')).grid(row=2, column=1)
ttk.Button(window, text='6', command=lambda: choice_number('6')).grid(row=2, column=2)
ttk.Button(window, text='7', command=lambda: choice_number('7')).grid(row=3, column=0)
ttk.Button(window, text='8', command=lambda: choice_number('8')).grid(row=3, column=1)
ttk.Button(window, text='9', command=lambda: choice_number('9')).grid(row=3, column=2)
ttk.Button(window, text='0', command=lambda: choice_number('0')).grid(row=4, column=0)

ttk.Button(window, text='+', command=lambda: choice_operator('+')).grid(row=1, column=3)
ttk.Button(window, text='-', command=lambda: choice_operator('-')).grid(row=2, column=3)
ttk.Button(window, text='*', command=lambda: choice_operator('*')).grid(row=3, column=3)
ttk.Button(window, text='/', command=lambda: choice_operator('/')).grid(row=4, column=3)
ttk.Button(window, text='C', command=clear_line).grid(row=4, column=1)
ttk.Button(window, text='=', command=rezult_calc).grid(row=4, column=2)


window.mainloop()
