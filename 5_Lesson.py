# HW_1
"""
i = 0
while True:
    if i == 3 or i == 13 or i == 23 or i == 33 or i == 43:
        print(i)
    if i > 43:
        break
    i += 1

# HW_2

pwd = ""
while len(pwd) < 8:
    pwd = input("Введите пароль не менее 8 символов: ")
print("Пароль принят")
"""

# HW_3

txt = "LADA 2010г 205000км 450000руб"
a, b, c, d = txt.split()
print(f"Продается автомобиль\nМарка: {a}\nГод выпуска: {b}\nПробег: {c}\nЦена: {d}")