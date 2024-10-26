from tkinter import *

'''
# функция Enumerate
fruits = ['яблоко', 'банан', 'киви', 'апельсин']
print(fruits)
s = 'киви'

for i, fruit in enumerate(fruits):
    if fruit == s:
        print(f"Фрукт {s} находится на позиции: {i+1}")
        break
'''


'''
# вычисление позиции мышки по клику
def mouse_click(event):
    print(f"Клик мыши на позиции: {event.x}, {event.y}")

window = Tk()

window.bind("<Button-1>", mouse_click)
window.mainloop()
'''

'''
# вычисление позиции мышки по движению
def mouse_move(event):
    print(f"Курсор на позиции: {event.x}, {event.y}")

window = Tk()

window.bind("<Motion>", mouse_move)
window.mainloop()
'''