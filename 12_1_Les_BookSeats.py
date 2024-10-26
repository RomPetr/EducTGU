from tkinter import *
from tkinter import messagebox as mb

# Бронирование мест

def check_seat(event=None):
    Num_seat = e_booking.get()
    e_booking.delete(0, END)
    try:
        if seats[Num_seat] == "Свободно":
            seats[Num_seat] = "Забронировано"
            show_seats_canvas()
            mb.showinfo("Успешно", f"Место {Num_seat} забронировано")
        else:
            mb.showerror(title="Ошибка", message="Место не забронировано")
    except KeyError:
        mb.showerror("Ошибка", f"Места {Num_seat} не существует")
    except Exception as exc:
        mb.showerror(title="Ошибка", message=f"Ошибка: {exc}")

def cancel_booking(event=None):
    Num_seat = e_cancel.get()
    e_cancel.delete(0, END)
    try:
        if seats[Num_seat] == "Забронировано":
            seats[Num_seat] = "Свободно"
            show_seats_canvas()
            mb.showinfo("Успешно", f"Бронь места {Num_seat} отменена")
        else:
            mb.showerror(title="Ошибка", message="Место не забронировано")
    except KeyError:
        mb.showerror("Ошибка", f"Места {Num_seat} не существует")
    except Exception as exc:
        mb.showerror(title="Ошибка", message=f"Ошибка: {exc}")
def show_seats_canvas():
    for i, (k, v) in enumerate(seats.items()):
        x = 50 * i + 5
        y = 100
        color = "green" if v == "Свободно" else "red"
        can.create_rectangle(x, y, x+40, y+40, fill=color)
        can.create_text(x+20, y+20, text=k)

seats = {f"А{i}": "Свободно" for i in range(10)}


window = Tk()

can = Canvas(window, width=500, height=250, bg="#dddce5")
can.pack(pady = 10)

show_seats_canvas()

e_booking = Entry(window, font=("Arial", 16))
e_booking.pack(pady=10)
e_booking.bind("<Return>", check_seat)
e_booking.focus()

btn = Button(window, text="Забронировать место", font=("Arial", 14), command=check_seat)
btn.pack(pady=10)

e_cancel = Entry(window, font=("Arial", 16))
e_cancel.pack(pady=10)
e_cancel.bind("<Return>", cancel_booking)

btn = Button(window, text="Отменить бронь", font=("Arial", 14), command=cancel_booking)
btn.pack(pady=10)

window.mainloop()

