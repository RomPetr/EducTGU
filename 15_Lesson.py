from tkinter import *
from tkinter import ttk
import calculator_logic as c

total_string = []

def rezult_calc():
    global total_string
    res = None
    second_number = float(line_input.get())
    line_input.delete(0, END)
    total_string.append(str(second_number))
    tot_str2 = str(total_string)
    total_label.config(text=tot_str2)
    if operator == "+":
        res = c.add(first_num, second_number)
    elif operator == '-':
        res = c.subtruct(first_num, second_number)
    elif operator == '*':
        res = c.multiply(first_num, second_number)
    elif operator == '/':
        res = c.divide(first_num, second_number)
    line_input.insert(0, res)
    total_string.append('=')
    total_string.append(str(res))
    print(total_string)
    tot_res = ' '.join(a for a in total_string)
    del(total_string[:])
    total_label.config(text=tot_res)




def choice_number(num):
    line_input.insert(END, num)


def choice_operator(oper):
    global total_string, operator, first_num
    first_num = float(line_input.get())
    operator = oper
    line_input.delete(0, END)
    total_string.append(str(first_num))
    total_string.append(operator)
    tot_str1 = str(total_string)
    total_label.config(text=tot_str1)


def clear_line():
    line_input.delete(0, END)


def validate_entry():
    li = line_input.get()
    num = ''.join(n for n in li if n in '0123456789.-')
    if li != num:
        line_input.delete(0, END)
        line_input.insert(0, num)


first_num = None
operator = None

window = Tk()
window.title("Калькулятор")
# window.wm_iconbitmap(bitmap="calculator_icon.ico")
line_input = Entry(window, font=('Arial', 12))
line_input.grid(row=0, column=0, columnspan=4, sticky='ew')
line_input.bind('<KeyRelease>', lambda event: validate_entry())

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

total_label = Label(text="...", font=("Arial", 12))
total_label.grid(row=5, column=2, columnspan=4, sticky='ew')

window.mainloop()
