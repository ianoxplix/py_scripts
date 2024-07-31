"""
Name: Izzy Jenrette
Course Number: CS-135-I01
Project Name: Priting my Initial
Description: This program prints my initials on the screen
"""

import turtle


screen = turtle.Screen()
screen.title("Drawing Initials IJ")


def draw_I():
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.pensize(13)  
    turtle.color("blue")  
    turtle.forward(0)  
    turtle.left(90)
    turtle.forward(100)
    turtle.penup()
    turtle.setheading(0)  

def draw_J():
    turtle.penup()
    turtle.goto(-25, 100)  
    turtle.pendown()
    turtle.pensize(8) 
    turtle.color("#FF5733")  
    turtle.forward(70)
    turtle.backward(80)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(70)
    turtle.circle(-40,120)
    turtle.penup()
    turtle.setheading(0)

draw_I()
draw_J()

turtle.hideturtle()
turtle.done()
