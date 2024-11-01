def add(a, b):
    return a + b


def subtruct(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return a / b
