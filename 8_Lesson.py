# now_smile = 128512
# while now_smile <= 128591:
#     print(chr(now_smile))
#     now_smile += 1
"""
# метод JOIN
sp = ['С', 'днем', 'рождения']
text = " ".join(sp)
print(f"{text} - {type(text)}")
"""

sp = []
count_items = int(input("Сколько эл-тов планируете ввести в список? "))
i = 0
while i < count_items:
    item = input("Введите число кроме нуля: ")
    if item.lstrip("-").isdigit():
        sp.append(int(item))
    else:
        sp.append(item)
    i += 1
print(sp)
