from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import pyperclip
import json
import os

history_file = "upload_history.json"


def save_history(file_path, link):
    history = []
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            history = json.load(f)
    history.append({"file_path": os.path.basename(file_path), "download_link": link})

    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)


def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://file.io', files=files)
                response.raise_for_status()
                link = response.json()['link']
                entry.delete(0, END)
                entry.insert(0, link)
                pyperclip.copy(link)
                save_history(filepath, link)
                mb.showinfo("Ссылка скопирована", f"Ссылка {link} успешно скопирована в буфер обмена")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")


def show_history():
    if not os.path.exists(history_file):
        mb.showinfo("История", "История загрузок пуста")
        return

    history_window = Toplevel(window)
    history_window.title("История загрузок")
    history_window.geometry("500x300")

    files_listbox = Listbox(history_window, width=200, height=50)
    files_listbox.grid(row=0, column=0, padx=(10, 0), pady=10)

    with open(history_file, "r") as f:
        history = json.load(f)
        for item in history:
            files_listbox.insert(END, f"Файл: {item['file_path']},  Ссылка: {item['download_link']}")


window = Tk()
window.title("Сохранение файлов в облаке")
window.geometry("450x200")


button = ttk.Button(text="Загрузить файл", command=upload)
button.pack(pady=10)

entry = ttk.Entry()
entry.pack(pady=10, padx=5, fill=X)

history_button = ttk.Button(text="Посмотреть историю", command=show_history)
history_button.pack(pady=10)

window.mainloop()
