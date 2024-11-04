"""
Добавьте в проект вторую базовую валюту, чтобы он выводил сразу два курса обмена одновременно.

    1. Добавьте еще одно поле для выбора второй базовой валюты.
    2. Измените функцию exchange так, чтобы она запрашивала и отображала курсы обмена для обеих базовых валют
       относительно выбранной целевой валюты.
"""
import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import pprint

"""
# --------------------------------------
# Получение курсов Топ 50 криптовалют из CoinGecko.com
url = "https://api.coingecko.com/api/v3/coins/markets"
response = requests.get(url, params={'vs_currency': 'usd', 'per_page': 50, 'page': 1})
data = json.loads(response.text)
p = pprint.PrettyPrinter(indent=3)
p.pprint(data)
# -------------------------------------
"""


def exchange():
    code = entry.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate} {code} за 1 доллар")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()
