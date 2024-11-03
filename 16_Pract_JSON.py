# курсы валют в формате JSON
import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb

"""
result = requests.get('https://open.er-api.com/v6/latest/USD')
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4)
p.pprint(data)
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
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {code} за 1 доллар")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты.")


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()