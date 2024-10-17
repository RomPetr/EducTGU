# import turtle as t
"""
t.ht()
r = 40
t.pensize(5)
t.color("#FF5A00")
t.fillcolor("#A200FF")
for i in range(6):
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.rt(60)
r = 30
for i in range(6):
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.rt(60)
#----------
t.ht()
r = 40
t.pensize(5)
t.color("#FF5A00")
t.fillcolor("#A200FF")
for j in range(4):
    for i in range(6):
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.rt(60)
    r = r - 10

t.ht()
r = 20
t.pensize(4)
t.color("#FF5A00")
t.fillcolor("#A200FF")
for j in range(4):
    for i in range(6):
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.rt(60)
    r = r - 5
t.pu()
t.fd(80)
t.pd()
r = 20
for j in range(4):
    for i in range(6):
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.rt(60)
    r = r - 5

t.ht()
r = 20
t.pensize(4)
t.color("#FF5A00")
t.fillcolor("#A200FF")
for k in range(3):
    for j in range(4):
        for i in range(6):
            t.begin_fill()
            t.circle(r)
            t.end_fill()
            t.rt(60)
        r = r - 5
    t.pu()
    t.fd(80)
    t.pd()
    r = 20

t.ht()
t.speed(0)
r = 20
t.pensize(4)
for r in range(40, 0, -10):
    for i in range(6):
        t.color(255, 165, r * 6)
        t.fillcolor(162, r * 6, 255)
        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.rt(60)

print(range(50, 4, -6)[1])
text = "Привет, как дела?"
s = text[:6] # можно без нуля
print(s)

text1 = "Это последние символы"
s = text1[-4:] # волы
print(s)

text = "12345678"
s = text[::2]
print(s) # 1357

text = "разделить строку"
x = 9
part1 = text[:x]
part2 = text[x:]
print(part1, part2)
"""
#----------
# HW_1
"""
import turtle as t

t.ht()
t.speed(0)
r = 20
t.pensize(1)
for r in range(40, 0, -10):
    for i in range(6):
        t.color(255, 165, r * 6)
        t.fillcolor(162, r * 6, 255)
        t.begin_fill()
        for j in range(4):
          t.forward(r)
          t.lt(90)

        t.end_fill()
        t.rt(60)
"""
# HW_2

import turtle as t

#t.ht()
t.speed(2)
#r = 20
t.pensize(1)
for r in range(40, 0, -10):
    for i in range(1):
        t.color(255, 165, r * 6)
        t.fillcolor(162, r * 6, 255)
        t.begin_fill()
        for j in range(6):
          t.forward(r)
          t.lt(120)
          t.forward(r / 2)
          t.lt(60)
          t.forward(r / 2)
          t.lt(60)
          t.forward(r / 2)
          t.lt(120)
          t.forward(r)
          t.lt(60)
        t.end_fill()
        t.lt(60)
        t.forward(r / 2)
        t.rt(60)


