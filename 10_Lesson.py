
from tkinter import *
"""
def change():
    metka['text'] = 'Черная метка'
    metka['bg'] = 'black'

window = Tk()
metka = Label(text="Привет всем!", bg="DarkRed", fg="LightSalmon", width=20, height=5)
metka.pack()
knopka = Button(text="Изменить метку", width=13, height=2)
knopka.config(command=change)
knopka.pack()
window.mainloop()
"""

"""
# инкремент
a = 1

def change():
    global a
    a += 1
    metka['text'] = a

window = Tk()
metka = Label(text='1', width=30, height=3)
metka.pack()
knopka = Button(text='Инкремент', width=30, height=3)
knopka.config(command=change)
knopka.pack()
window.mainloop()
"""

"""
# смайлики
a = 128512

def change():
    global a
    a += 1
    metka['text'] = chr(a)

window = Tk()
metka = Label(text=chr(a), font='Arial 64')
metka.pack()
knopka = Button(text='Следующий смайлик', width=30, height=3)
knopka.config(command=change)
knopka.pack()
window.mainloop()
"""

"""
# Фреймы
window = Tk()
frame_top = Frame(window)
frame_bottom = Frame(window)
frame_top.pack()
frame_bottom.pack()

metka1 = Label(frame_top, text='Метка 1', bg = 'red')
metka1.pack(side=LEFT)
metka2 = Label(frame_top, text='Метка 2', bg = 'yellow')
metka2.pack(side=RIGHT)
metka3 = Label(frame_bottom, text='Метка 3', bg = 'green')
metka3.pack(side=LEFT)
metka4 = Label(frame_bottom, text='Метка 4', bg = 'blue')
metka4.pack(side=RIGHT)
window.mainloop()
"""

# Поле ввода

def read():
    name = e.get()
    print(name)
    e.delete(0, END)

def read2():
    city = e2.get()
    print(city)
    e2.delete(0, END)

window = Tk()
f1 = Frame()
f2 = Frame()
f1.pack()
f2.pack()
m = Label(f1, text='Введите имя:', bg='grey', fg='white', font='Courier 18 bold')
m.pack(side=LEFT)
e = Entry(f1, width=50, justify='left', bg='grey', fg='white', font='Courier 18 bold')
e.pack(side=LEFT)
b = Button(f1, text='Ввод', bg='grey', fg='white', font='Courier 18 bold', command=read)
b.pack()

m2 = Label(f2, text='Введите город:', bg='grey', fg='white', font='Courier 18 bold')
m2.pack(side=LEFT)
e2 = Entry(f2, width=50, justify='left', bg='grey', fg='white', font='Courier 18 bold')
e2.pack(side=LEFT)
b2 = Button(f2, text='Ввод', bg='grey', fg='white', font='Courier 18 bold', command=read2)
b2.pack()
window.mainloop()


"""Объединение списков без цикла"""

# my_list = [[10, 20, 30], [40, 50], [60], [70, 80, 90]]
# print(sum(my_list, []))  # -> [10, 20, 30, 40, 50, 60, 70, 80, 90]

"""
# Оператор is
from sys import getrefcount

a = [10, 20, 30, 40]
print(getrefcount(a))
b = [10, 20, 30, 40]

print(a == b)  # равенство по значению
print(a is b)  # равенство по ссылке

a = 'a'
print(getrefcount(a))
b = 1
c = 1
print(a == b)
print(a is b)

c = a[:]
c.append(1)
print(c)
print(a)

a = 1
b = 1

a, b = 1, 2

print(a == b)
print(a is b)

if a is b:
    print("Переменные идентичны")
else:
    print("Переменные не идентичны")

'''Переменные идентичны'''

obj_1 = [10, 20, 30, 40]
obj_2 = obj_1
print(obj_1 == obj_2)  # -> True
print(obj_1 is obj_2)  # -> True

obj_2 = obj_1[:]  # переменная obj_2 ссылается на копию obj_1
print(obj_1 == obj_2)  # -> True
print(obj_1 is obj_2)  # -> False
print(obj_1 is not obj_2)  # -> True

obj_1 = None
print(obj_1 is None)  # -> True
"""