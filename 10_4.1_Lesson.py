from tkinter import *

# словари
'''
slo = {"A1": "Яблоко", "A2": "Банан", "A3": "Киви"}
print(slo["A1"]) # выведет Яблоко

users = {"user1": {"name": 'Иван', "age": 27, "pass": '12345'},
       "user2": {"name": 'Максим', "age": 32, "pass": 'qwe123'}}
for i in users.items():
    print(i)
for i in users.values():
    print(i)
for i in users.keys():
    print(i)
'''

'''
# вывод каждого элемента словаря
users = {"user1": {"name": 'Иван', "age": 27, "pass": '12345'},
       "user2": {"name": 'Максим', "age": 32, "pass": 'qwe123'}}
for key, value in users.items():
    print(key)
    for j in value.items():
        print(f"{j[0]} - {j[1]}")
    print()
'''

"""
# добавление элементов в словарь
users = {1: "Tom", 2: "Bob", 3: "Bill"}
users[4] = "Maria" # добавит эл-т с ключем 4
print(users)
"""

"""
# удаление элементов словаря
users = {1: "Tom", 2: "Bob", 3: "Bill"}
users.pop(1)
print(users)
del users[3]
print(users)
"""


# модуль tkinter
"""
counter = 0
def clicker():
	global counter
	counter += 1
	text_m.config(text=counter)

window = Tk()
text_m = Label(window,
			   text="0",
			   bg="#5aa836",
			   fg='white',
			   font=("Arial", 18),
			   width=20,
			   height=3)
text_m.pack()
btn = Button(window, text="Click me", bg="black", fg="yellow",
			 activebackground="#d1a413", activeforeground="#d15813",
			 font=("Arial", 16), width=20, command=clicker)
btn.pack()
window.mainloop()
"""

"""
def check_entry():
	data = e1.get()
	data2 = e2.get()
	if data and data:
		t_m.config(text="Данные отправлены")
		t_m.config(fg="green")
		print(data)
		print(data2)
		e1.delete(0, END)
		e2.delete(0, END)
	else:
		t_m.config(text="Одно или несколько полей не заполнены", font=("Arial", 10))
		t_m.config(fg="red")

window = Tk()

e1 = Entry(window, width=22, font=('Arial', 16), justify="left")
e1.pack(pady=[10,10])

e2 = Entry(window, width=22, font=('Arial', 16))
e2.pack(pady=[10,10])

t_m = Label(window, text="")
t_m.pack()

btn = Button(window, text="Отправить", command=check_entry)
btn.pack(pady=[10,10])

window.mainloop()
"""


# фреймы
import re
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
name_label = ttk.Label(frame, text="Введите имя")
name_label.pack(anchor=NW)

name_entry = ttk.Entry(frame)
name_entry.pack(anchor=NW)

frame.pack(anchor=NW, fill=X, padx=5, pady=5)

root.mainloop()

