"""
from tkinter import *
from tkinter import filedialog as fd

def text_load():
    file = fd.askopenfilename()
    if file:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        t.delete(1.0, END)
        t.insert(1.0, content)

def text_save():
    file = fd.asksaveasfilename(filetypes=(("TXT Files", "*.txt"), ("All Files", "*.*")))
    if file:
        with open(file, "w", encoding="utf-8") as f:
            content = t.get(1.0, END)
            f.write(content)

window = Tk()

t = Text(window, width=50, height=10)
t.pack()

btn1 = Button(window, text="Загрузить текст", command=text_load)
btn1.pack()

btn2 = Button(window, text="Сохранить текст", command=text_save)
btn2.pack()

window.mainloop()
"""

"""
# радиокнопки
import tkinter as tk

root = tk.Tk()

# Создаем переменную для хранения значения выбранной радиокнопки
selected_option = tk.StringVar(value="Option1")

# Создаем радиокнопки и связываем их с переменной selected_option
radio1 = tk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option2")
radio3 = tk.Radiobutton(root, text="Option 3", variable=selected_option, value="Option3")

radio1.pack()
radio2.pack()
radio3.pack()

# Функция для получения текущего значения переменной
def show_selected():
    print("Текущая выбранная опция:", selected_option.get())

# Кнопка для вызова функции show_selected
button = tk.Button(root, text="Показать выбранную опцию", command=show_selected)
button.pack()

root.mainloop()
"""

"""
# изменения свойств кнопки
import tkinter as tk

root = tk.Tk()

# Создаем кнопку с начальными параметрами
button = tk.Button(root, text="Нажми меня", bg="blue", fg="white")
button.pack(pady=20)

# Функция для изменения свойств кнопки
def change_button_properties():
    button.config(text="Изменено!", bg="green", fg="black", font=("Arial", 14))

# Кнопка для изменения свойств первой кнопки
change_button = tk.Button(root, text="Изменить свойства", command=change_button_properties)
change_button.pack(pady=20)

root.mainloop()
"""

greeting = "Hello, world!"
print(greeting[:5])