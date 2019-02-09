
"""Student Name: Vrushali Kadam
Student id: 1001514762
Turtle Graphics Drawings
Use the turtle graphics library to write programs that reproduce each of the designs shown.
"""

import turtle
vru = turtle.Turtle()
vru.hideturtle()
for x in range(5):
    if(x%2==0):
        vru.pendown()
        vru.circle(50)
    else:
        vru.penup()
        vru.forward(125)
vru.setheading(135)
vru.penup()
vru.forward(70)
vru.left(45)
vru.forward(10)
vru.pendown()
vru.circle(50)
vru.penup()
vru.forward(125)
vru.pendown()
vru.circle(50)

        
    
