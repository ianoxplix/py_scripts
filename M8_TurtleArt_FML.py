# Author: Your Name
# Project: Original Graphic Art
# Date: Today's Date

import turtle,random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("lightblue")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)

# Draw concentric circles with different colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
radius = 280





def draw_circle(radius, color):
    t.color(color)  # Set the color for the circle
    t.begin_fill()  # Start filling the circle with color
    t.circle(radius)  # Draw the circle
    t.end_fill() 

for color in colors:
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    radius += 40

# Draw lines from the center
num_circles = 30  # Number of circles to draw
max_radius = 200  # Maximum radius for the outermost circle

for i in range(num_circles):
    radius = max_radius - (i * (max_radius / num_circles))
    color = random.choice(colors)
    draw_circle(radius, color)
    t.penup()
    t.goto(0, -radius)  # Re-center for the next circle
    t.pendown()

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()

