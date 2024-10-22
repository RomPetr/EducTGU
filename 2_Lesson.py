import turtle as t
# print(range(4))
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)

"""
ugol = int(input("Введите количество углов: "))
turtle.color("red")
turtle.begin_fill()
for i in range(ugol):
    turtle.forward(80)
    turtle.left(360 / ugol)
turtle.end_fill()
#----------
ugol = int(input("Введите количество углов: "))
Col = input("Введите цвет на английском: ")
turtle.color(Col)
turtle.begin_fill()
for i in range(ugol):
    turtle.forward(80)
    turtle.left(360 / ugol)
turtle.end_fill()
#----------
t.begin_fill()
t.color("red")
t.circle(50)
t.end_fill()
t.penup()
t.forward(70)
t.pendown()
t.begin_fill()
t.color(245, 66, 179)
t.circle(50)
t.end_fill()
#-----------
r = input("Введите радиус: ")
for i in range(3):
    t.begin_fill()
    t.color(255, 50, 80 * i)
    t.circle(50)
    t.end_fill()
    t.penup()
    t.forward(70)
    t.pendown()
#----------
for i in range(30):
    t.color(255, 255, 10 * i)
    t.circle(i)
#----------
for i in range(10, 100, 5):
    t.color("blue")
    t.circle(i)
    t.lt(90)

# Zvezda
ugol = int(input("Введите количество углов: "))
Col = input("Введите цвет на английском: ")
turtle.color(Col)
turtle.begin_fill()
for i in range(ugol):
    turtle.forward(80)
    turtle.left(360 * 2 / ugol)
turtle.end_fill()
"""
""""
HW_1
1.  Нарисуйте три разных круга, используя разные цвета и радиусы, используя модуль turtle. 
Для каждого круга используйте begin_fill(), color(), circle() и end_fill().    

t.penup()
for i in range(3):
    t.begin_fill()
    t.color(26 * i + 20, 50 * i - 40, 80 * i + 40)
    t.circle(i * 2 + 20)
    t.forward(60)
    t.end_fill()
"""

"""
2.  Используя методы модуля turtle, нарисуйте несколько геометрических фигур: 
прямоугольник, ромб и трапецию. Каждая фигура должна быть закрашена в свой цвет, 
который сочетается с остальными. Используйте цветовой круг Adobe для выбора красивого сочетания цветов.

import turtle as t

len = 100
tri = 120

# прямоугольник
t.begin_fill()
t.color(89, 240, 123)
for i in range(4):

    if (i == 1 or i == 3):
        len = len / 2
    else:
        len = 100
    t.forward(len)
    t.left(90)
t.end_fill()

# ромб
t.up()
t.goto(-100, 0)
t.down()
t.begin_fill()
t.color(186, 240, 89)
for i in range(4):
    if (i == 1 or i == 3):
        tri = tri / 2
    else:
        tri = 120
    t.forward(len / 2)
    t.right(tri)
t.end_fill()

# трапеция
t.up()
t.goto(-50, -50)
t.down()
t.begin_fill()
t.color(89, 238, 240)
for i in range(4):
    if (i == 0):
        tri = 0
        len = 100
        t.right(tri)
        t.forward(len)

    if (i == 1):
        tri = 60
        len = 50
        t.right(tri)
        t.forward(len)

    if (i == 2):
        tri = 120
        len = 140
        t.right(tri)
        t.forward(len)

    if (i == 3):
        tri = 110
        len = 50
        t.right(tri)
        t.forward(len)

t.end_fill()

3.  Нарисуйте зеленую елку из трех закрашенных треугольников.

import turtle as t

len = 100
tri = 120

t.up()
t.goto(0, -100)
# треугольник
t.begin_fill()
t.color(89, 240, 123)
for i in range(3):
  t.forward(len)
  t.left(tri)
t.end_fill()

#t.up()
t.goto(0, -20)
# треугольник
t.begin_fill()
t.color(89, 240, 123)
for i in range(3):
  t.forward(len)
  t.left(tri)
t.end_fill()

t.goto(0, 60)
# треугольник
t.begin_fill()
t.color(89, 240, 123)
for i in range(3):
  t.forward(len)
  t.left(tri)
t.end_fill()
"""

"""
4.  Нарисуйте три квадрата размером 30 на 30 на расстоянии 30 пикселей друг от друга. 
Квадраты не должны соединятся зеленой линией.
"""
import turtle as t
t.colormode(255)

t.up()
t.goto(-100, 0)
t.down()
t.pensize(5)
# квадрат
t.begin_fill()
t.color('red', 'blue')
for i in range(4):
  t.forward(30)
  t.left(90)
t.end_fill()

t.up()
t.goto(-40, 0)
t.down()
# квадрат
t.begin_fill()
t.color(255, 127, 80)
for i in range(4):
  t.forward(30)
  t.left(90)
t.end_fill()

t.up()
t.forward(60)
t.down()
# квадрат
t.begin_fill()
t.color("green", "black")
for i in range(4):
  t.forward(30)
  t.left(90)
t.end_fill()

t.done()