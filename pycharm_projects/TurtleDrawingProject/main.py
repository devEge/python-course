import turtle

# Screen Configuration
drawing_board = turtle.Screen()
drawing_board.bgcolor("#2D2F31")
drawing_board.title("Python Turtle")

# Turtle Instance
ti = turtle.Turtle()

# Star Drawing
for i in range(5):
    ti.right(144)
    ti.forward(100)

# Closes The Turtle
turtle.done()
