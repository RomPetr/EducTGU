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