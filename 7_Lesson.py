import datetime
import math
import random
"""
t = datetime.datetime.now()
print("Текущее время: ", t)

d = datetime.date.today()
print("Текущая дата: ", d)
date = d.strftime("%d-%m-%Y")
date1 = d.strftime("%c")
print("Форматированная дата: ", date)
print("Местная версия даты и времени: ", date1)
"""

# Из семинара
"""
d = datetime.date.today()
mon = d.month
sp_month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь",
            "Ноябрь", "Декабрь"]
mon_ru = sp_month[mon - 1 ]
print(f"Сегодня: {d.day} {mon_ru} {d.year}")
"""

"""
num = int(input("Введите число: "))
k_num = math.sqrt(num)
print(f"{k_num:.4f} - корень числа {num}")
"""

"""
# нахождение индекса в кортеже
k = (1, 4, 5, 8, 75, 694)
while True:
    number = int(input("Введите цифру, индекс которой вы хотите узнать: "))
    if number == 0:
        print("Конец работы программы")
        break
    if number in k:
        ind = k.index(number)
        print(f"Индекс {number} - {ind}\n")
    else:
        print(f"Такой цифры нет в кортеже\n")
"""

"""
# перебор списка в цикле
sp = ['Hello', 'apple', 'kiwi']
i = 0
while i < len(sp):
    print(sp[i])
    i += 1
"""
# случайные имена и профессии
"""
name = ["Петя", "Вася", "Аскольд", "Шурик", "Снежана"]
job = ["плотник", "маляр", "доставщик", "двоечник", "балерина", "программист", "космонавт"]
rnd_name = random.randint(0, 4)
rnd_job = random.randint(0, 6)
age = random.randint(5, 25)
print(f"Меня зовут {name[rnd_name]} мне {age} лет, я {job[rnd_job]}")
"""

"""
name = []
job = []
names = int(input("Сколько имен введете? "))
jobs = int(input("Сколько профессий введете? "))
for i in range(names):
    name.append(input("Введите имя: "))
for i in range(jobs):
    job.append(input("Введите профессию: "))
print(name)
print(job)

rnd_name = random.randint(0, len(name) - 1)
rnd_job = random.randint(0, len(job) - 1)

print(f"Меня зовут {name[rnd_name]} я {job[rnd_job]}")
"""

"""
# for i in range(256):
#    print(f"Символ {chr(i)} код символа {i}")

alf = 'abcdefghijklmnopqrstuvwxyz'
for i in alf:
    print(f"Код символа {i} - {ord(i)}")
"""
print(f"Миша{chr(9825)}Маша")

# s = [1,2,3]
# print(s*2)