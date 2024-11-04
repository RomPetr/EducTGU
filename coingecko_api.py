import tkinter as tk
from tkinter import ttk
import requests

# Функция для получения данных о криптовалютах
def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 50,
        'page': 1,
        'sparkline': False,
    }
    response = requests.get(url, params=params)
    return response.json()

# Функция для обновления информации о выбранной криптовалюте
def update_price(event):
    selected_coin = combo.get()
    for coin in crypto_data:
        if coin['name'] == selected_coin:
            price_label.config(text=f"Цена: ${coin['current_price']:.2f}")
            break

# Получение данных о криптовалютах
crypto_data = get_crypto_data()

# Создание основного окна приложения
root = tk.Tk()
root.title("Курс криптовалют")

# Создание выпадающего списка
crypto_names = [coin['name'] for coin in crypto_data]
combo = ttk.Combobox(root, values=crypto_names)
combo.bind("<<ComboboxSelected>>", update_price)
combo.pack(pady=10)

# Метка для отображения цены
price_label = tk.Label(root, text="Выберите криптовалюту")
price_label.pack(pady=10)

# Запуск основного цикла приложения
root.mainloop()