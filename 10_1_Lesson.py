from tkinter import *

"""
# Проект “Инкремент”
a = 0
def change():
    global a
    a += 1
    metka['text'] = str(a)

window = Tk()
metka = Label(text="0",
              bg="Pink",
              fg="MediumVioletRed",
              width=30,
              height=3)
metka.pack()
knopka = Button(text="Инкремент",
                width=15,
                height=3)
knopka.config(command=change)
knopka.pack()
window.mainloop()
"""

"""
Задание:
Сделай программу “Декремент”, которая будет уменьшать число, показанное на метке, на 1
при каждом нажатии на кнопку. Начальное значение числа на метке равно 100.


a = 100
def change():
    global a
    a -= 1
    metka['text'] = str(a)
    if a % 2 == 0:
        metka['bg'] = "Yellow"
    else:
        metka['bg'] = "Green"

window = Tk()
metka = Label(text="100",
              bg="#ba99de",
              fg="MediumVioletRed",
              width=20,
              height=3)
metka.pack()
knopka = Button(text="Декремент",
                bg="LimeGreen",
                fg="IndianRed",
                width=15,
                height=2)
knopka.config(command=change)
knopka.pack()
window.mainloop()
"""

"""
# Кнопка вввода читает текст из Entry и выводит его в консоль
def read():
    Name = e.get()
    print(Name)

window = Tk()
m = Label(text="Введите имя", bg="gray", font="Courier 16")
m.pack(side=LEFT)
e = Entry(width=20, justify="left", bg="gray", fg="white", font="Courier 18 bold")
e.pack(side=LEFT)
b = Button(text="Ввод", bg="grey", font="Courier 12 bold", command=read)
b.pack(side=LEFT)
window.mainloop()
"""


# многострочное текстовое поле

def read():
    t = text.get(1.0, END)
    print(t)

def insert():
    pushkin = "Я помню чудное мгновенье: передо мной явилась ты, \
    как мимолетное виденье, как гений чистой красоты. \
    В томленьях грусти безнадежной, \
    в тревогах шумной суеты, звучал мне долго голос нежный \
    и снились милые черты."
    T = text.insert(1.0, pushkin)
    print(T)

def delete():
    text.delete(1.0, END)

window = Tk()
text = Text(width=30, height=8, bg='black', fg='white')
text.pack(side=LEFT)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
b = Button(text="ввод", command=read)
b.pack(side=LEFT)
b2 = Button(text="вставка", command=insert)
b2.pack(side=LEFT)
b3 = Button(text='удаление текста', command=delete)
b3.pack(side=LEFT)
window.mainloop()
