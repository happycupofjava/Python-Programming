
"""Student Name: Vrushali Kadam
Student id: 1001514762
Turtle Graphics Drawings
Use the turtle graphics library to write programs that reproduce each of the designs shown.
"""

import turtle
vru = turtle.Turtle()
vru.hideturtle()
vru.dot()
for x in range(7):
    if(x%2 == 0):
        vru.pendown()
    else:
        vru.penup()
    vru.forward(20)
vru.dot()
vru.left(90)
vru.forward(140)
vru.dot()
vru.left(90)
for x in range(7):
    if(x%2 == 0):
        vru.pendown()
    else:
        vru.penup()
    vru.forward(20)
vru.dot()
vru.left(90)
vru.forward(140)
vru.dot()
vru.left(135)
vru.forward(197.98)
vru.right(135)
vru.forward(140)
vru.right(135)
vru.forward(197.98)
vru.back(98.99)
vru.dot()


