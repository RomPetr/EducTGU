# функции
"""
def add(n):
    rez = 0
    for i in range(1, n+1):
        rez += i
    return rez

num = int(input("Введите число, для нахождеия суммы чисел от 1 до этого числа: "))
rez = add(num)
print(rez)
"""

"""
# калькулятор
def add(a, b):
    return a + b

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "На ноль делить нельзя"

print("Выберите действие:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choise = input("Введите номер операцим (1/2/3/4):")
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if choise == "1":
    print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
elif choise == "2":
    print(f"Результат: {num1} - {num2} = {sub(num1, num2)}")
elif choise == "3":
    print(f"Результат: {num1} * {num2} = {mul(num1, num2)}")
elif choise == "4":
    rez = div(num1, num2)
    if (isinstance(rez, str)):
        print(rez)
    else:
        print(f"Результат: {num1} / {num2} = {rez}")
"""
# -----Телефонный справочник------
contacts = {}

def input_contact():
    name = input("Введите имя: ")
    phone = input("Введите десятизначный номер телефона, начинающийся с 9: ")
    if len(phone) == 10 and phone.isdigit() and phone.startswith("9"):
        contacts[name] = phone
        print("контакт успешно добавлен")
        print(contacts)
    else:
        print("Ошибка! Неверный номер телефона.")

def find_contact():
    name = input("Введите имя для поиска: ")
    print(contacts.get(name, "Контакт не найден"))

def delete_contact():
    name = input("Введите имя для удаления")
    try:
        del contacts[name]
        print(contacts)
        print("Контакт успешно удален")
    except KeyError:
        print("Контакт не найден")

while True:
    action = input("Выберите действие: добавить (1), найти (2), удалить (3), выйти (4)")
    if action == "1":
        input_contact()
    elif action == "2":
        find_contact()
    elif action == "3":
        delete_contact()
    elif action == "4":
        break



# работа с файлами
"""
try:
    file = open("TestFile.txt", "r", encoding = "utf-8")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Файл не найден на компьютере")
except Exception as exc:
    print(f"Ошибка - {exc}")
"""

"""
try:
    with open("TestFile.txt", "r", encoding = "utf-8") as file: # не нужен file.close()
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден на компьютере")
except Exception as exc:
    print(f"Ошибка - {exc}")
"""

"""

try:
    with open("TestFile.txt", "a", encoding = "utf-8") as file: # не нужен file.close()
        content = file.write("Хорошая погода!\n")
        print(content)
except FileNotFoundError:
    print("Файл не найден на компьютере")
except Exception as exc:
    print(f"Ошибка - {exc}")
"""

"""
# бронирование мест
# список мест будет в виде списка кортежей
# [('Б1', 'свободно'), ('Б2', 'свободно')]

def book_seat(seats):
    seat_name = input("Введите место для бронирования (от Б1 до Б9): ")
    try:
        i = seats.index((seat_name, "свободно"))
        seats[i] = (seat_name, "забронировано")
        print(f"Место {seat_name} успешно забронировано.")
    except ValueError:
        print(f"Место {seat_name} уже забронировано или не существует.")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")

seats = [(f"Б{i}", "свободно") for i in range(1, 10)]
print(seats)

while True:
    book_seat(seats)
    booking = input("Хотите забронировать еще одно место? (да/нет): ")
    if booking.lower() != "да":
        break

print("Итоговое состояние бронирования мест.")
for seat in seats:
    print(f"{seat[0]}: {seat[1]}")
"""

"""
# подсчет кол-ва слов в файле
def count(file_name):
    try:
        with open(file_name, encoding = 'utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

words = count("proba.txt")
print(f"Количество слов в файле: {words}")
"""

"""
# анализ файла с логом
def analyze_log(file_name):
    counter = {"INFO":0, "ERROR":0, "WARNING":0}

    try:
        with open(file_name) as file:
            for line in file:
                if "[INFO]" in line:
                    counter["INFO"] += 1
                elif "[ERROR]" in line:
                    counter["ERRROR"] += 1
                elif "[WARNING]" in line:
                    counter["WARNING"] += 1
        for k, v in counter.items():
            print(f"{k}: {v}")
    except FileNotFoundError:
        print(f "Файл {file_name} не найден.")
    except Exception as e:
        print(f"Произошла следующая ошибка: {e}")

analyze_log('log.txt')
"""
#HW_1
"""
Создайте программу на Python, которая подсчитает сколько строк содержит название фирмы NEC, сколько SHARP и сколько SONY.
Результат должен быть выведен в консоль в следующем виде:
NEC: 36
SHARP: 24
SONY:40

def log_anlz(file_name):
    counter = {"NEC":0, "SHARP":0, "SONY":0}

    try:
        with open(file_name) as file:
            for line in file:
                if "Protocol=NEC" in line:
                    counter["NEC"] += 1
                elif "Protocol=SHARP" in line:
                    counter["SHARP"] += 1
                elif "Protocol=SONY" in line:
                    counter["SONY"] += 1
        for k, v in counter.items():
            print(f"{k}: {v}")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
    except Exception as e:
        print(f"Произошла следующая ошибка: {e}")

log_anlz('Demo.log')
"""