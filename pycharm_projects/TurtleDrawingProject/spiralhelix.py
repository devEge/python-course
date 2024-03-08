import turtle

# Screen Configuration
drawing_board = turtle.Screen()
drawing_board.bgcolor("black")
drawing_board.title("Python Turtle")

# Turtle Instance
ti = turtle.Turtle()
ti.speed(0)
ti.width(2)
ti.color("#6495ED")

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(1, 50):
    ti.circle(5 * i)
    ti.circle(-5 * i)
    ti.color(colors[i % len(colors)])
    ti.left(i)

# Closes The Turtle
turtle.done()
