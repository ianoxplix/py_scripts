"""
Name:Izzy Jenrette
Unit Code:CS-135-I01
Project Name:Turtle tinkering 
Description:
    This program will draw a staircase using the turtle graphics library.
    The user can input the number of steps (1-4), and the program will systematically
    change the color and increase the pen width for each step the user inputed.
"""

import turtle

# Seting up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Creating a turtle object
stairs = turtle.Turtle()
stairs.speed(1)

# Define the colors and pen widths for each step
colors = ["red", "green", "blue", "purple"]
pen_widths = [3, 8, 12, 16]

# Get the user input for the number of steps (1-4)
num_steps = int(input("Enter the number of steps (1-4): "))

# Ensure that the number of steps is within the valid range
if num_steps < 1:
    num_steps = 1
elif num_steps > 4:
    num_steps = 4

# Draw the steps
for i in range(num_steps):
    stairs.color(colors[i])
    stairs.pensize(pen_widths[i])
    stairs.forward(50)
    stairs.left(90)
    stairs.forward(50)
    stairs.right(90)


