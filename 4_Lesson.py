T = input("Укажите значение температуры воды в озере: ")

if T.isdigit() or (T[0] == '-' and T[1:].isdigit()):
    T = int(T)
    if T <= 0:
        print("Озеро замерзло")
    elif T > 0 and T < 10:
        print("Ледяная вода")
    elif T >= 10 and T < 15:
        print("Жуть как холодно")
    elif 15 <= T < 18:
        print("Прохладно, но можно купаться")
    elif 18 <= T < 24:
        print("Кайф")
    elif 24 <= T < 30:
        print("Полный кайф")
    elif T >= 30 and T < 36:
        print("Горячая")
    else:
        print("Кипяток")
else:
    print("Вы ввели не число")