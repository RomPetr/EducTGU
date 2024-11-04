# курсы валют в формате JSON
import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

"""
result = requests.get('https://open.er-api.com/v6/latest/USD')
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4)
p.pprint(data)
"""


def update_currency_label(event):
    # Получаем полное название валюты из словаря и обновляем метку
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)


def update_base_label(event):
    # Получаем полное название валюты из словаря и обновляем метку
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)

def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()

    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status() # Проверяем, не произошла ли ошибка HTTP
            data = response.json()
            # print(data)

            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code]
                target = currencies[target_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {target} за 1 {base}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты.")


currencies = {
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'GBP': 'Британский фунт стерлингов',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахский тенге',
    'UZS': 'Узбекский сум',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар',
    'USD': 'Американский доллар'
}


# Создание графического интерфейса
window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x260")

Label(text="Базовая валюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_base_label)

base_label = ttk.Label()
base_label.pack(padx=10, pady=10)

Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
