# Функции Калькулятор

def get_number(prompt):
    while True:
        value = input(prompt)
        if value.lstrip('-').isdigit():
            return int(value)
        else:
            print("Это не целое число.")

add = lambda x, y: x + y
subtruct = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: "Ошибка! Деление на ноль!" if y == 0 else x / y

# def add(x, y):
#     return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        print("Ошибка. Деление на ноль.")
    else:
        return x / y

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

valid_choices = ['1', '2', '3', '4']
choise = None

while choise not in valid_choices:
    choise = input("Введите номер операции: 1/2/3/4: ")
    if choise not in valid_choices:
        print("Вы ввели не 1, не 2, не 3 и не 4.")

num1 = get_number("Введите первое целое число: ")
num2 = get_number("Введите второе целое число: ")

if choise == '1':
    print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
elif choise == '2':
    print(f"Результат: {num1} - {num2} = {sub(num1, num2)}")
elif choise == '3':
    print(f"Результат: {num1} * {num2} = {mul(num1, num2)}")
elif choise == '4':
    result = divide(num1, num2)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Результат: {num1} / {num2} = {result:.2f}")
else:
    print("Неверный выбор операции.")