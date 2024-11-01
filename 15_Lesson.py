from tkinter import *
from tkinter import ttk
import calculator_logic as c


window = Tk()
window.title("Калькулятор")
# window.wm_iconbitmap(bitmap="calculator_icon.ico")
line_input = Entry(window, font=('Arial', 12))
line_input.grid(row=0, column=0, columnspan=4, sticky='ew')

ttk.Button(window, text='1').grid(row=1, column=0)
ttk.Button(window, text='2').grid(row=1, column=1)
ttk.Button(window, text='3').grid(row=1, column=2)
ttk.Button(window, text='4').grid(row=2, column=0)
ttk.Button(window, text='5').grid(row=2, column=1)
ttk.Button(window, text='6').grid(row=2, column=2)
ttk.Button(window, text='7').grid(row=3, column=0)
ttk.Button(window, text='8').grid(row=3, column=1)
ttk.Button(window, text='9').grid(row=3, column=2)
ttk.Button(window, text='0').grid(row=4, column=0)
ttk.Button(window, text='+').grid(row=1, column=3)
ttk.Button(window, text='-').grid(row=2, column=3)
ttk.Button(window, text='*').grid(row=3, column=3)
ttk.Button(window, text='/').grid(row=4, column=3)
ttk.Button(window, text='C').grid(row=4, column=1)
ttk.Button(window, text='=').grid(row=4, column=2)


window.mainloop()
