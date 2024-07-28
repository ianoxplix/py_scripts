# Created by: [Your Name]
# Project: Turtle Graphics Art
# Date: [Today's Date]

import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)

# Create a turtle object
artist = turtle.Turtle()
artist.speed(0)  # Set to fastest speed
artist.hideturtle()  # Hide the turtle cursor

# Define the colors to be used in the artwork
colors = ["red", "yellow", "blue", "green", "purple", "orange", "pink"]

# Function to draw a circle with a given radius and color
def draw_circle(radius, color):
    artist.color(color)
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()

# Draw concentric circles with random colors and decreasing radius
num_circles = 30  # Number of circles to draw
max_radius = 200  # Maximum radius for the outermost circle

for i in range(num_circles):
    radius = max_radius - (i * (max_radius / num_circles))
    color = random.choice(colors)
    draw_circle(radius, color)
    artist.penup()
    artist.goto(0, -radius)  # Re-center for the next circle
    artist.pendown()

# Keep the window open until it is closed by the user
screen.mainloop()
