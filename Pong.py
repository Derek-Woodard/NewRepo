# Pong made in Python - the start to re-learning code

# Ipmort a base game to build on top of
import turtle

# Create a window
win = turtle.Screen()

# give the window a title
win.title("Pong through tutorial")

# Set the background colour of the screen to be black
win.bgcolor("black")

# Set the size of the window
win.setup(width=800, height=600)

# Stops the window from updating - allows us to manually update - adds speed
win.tracer(0)

# Paddle A
# Create a turtle object as the paddle
paddle_a = turtle.Turtle()
# Sets speed to max possible speed
paddle_a.speed(0)
# Give the paddle a shape using a built in shape through turtle
paddle_a.shape("square")
paddle_a.color("white")
# Default size of the square shape is 20 x 20
# Change the size of the paddle by multiplying the width by 5, and the length by 1
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
# The turtle program draws lines as it moves - the following stops the line from appearing
paddle_a.penup()
# Set the starting posistion of the paddle to the left side of the screen - (0,0) is the center of the screen
paddle_a.goto(-350,0)


# Paddle B
# Create a turtle object as the paddle
paddle_b = turtle.Turtle()
# Sets speed to max possible speed
paddle_b.speed(0)
# Give the paddle a shape using a built in shape through turtle
paddle_b.shape("square")
paddle_b.color("white")
# Default size of the square shape is 20 x 20
# Change the size of the paddle by multiplying the width by 5, and the length by 1
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
# The turtle program draws lines as it moves - the following stops the line from appearing
paddle_b.penup()
# Set the starting posistion of the paddle to the left side of the screen - (0,0) is the center of the screen
paddle_b.goto(350,0)


# Ball

# Main game loop
while True:
    win.update()