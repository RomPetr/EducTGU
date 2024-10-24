# вычисляем положение окна
from tkinter import *

window = Tk()
window.title("Главное окно")
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
print(f"Размер вашего экрана {w} на {h} пикселей")
w1 = w // 2 - 200
h1 = h // 2 - 150
window.geometry(f"400x300+{w1}+{h1}")
window.mainloop()