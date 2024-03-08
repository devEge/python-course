import turtle

# Screen Configuration
drawing_board = turtle.Screen()
drawing_board.bgcolor("#2D2F31")
drawing_board.title("Python Turtle")

# Turtle Instance
ti = turtle.Turtle()
ti.color("#6495ED")

def shrinkingsquare(size):
    for i in range(4):
        ti.forward(size)
        ti.left(90)
        size -= 5


for i in range(7):
    shrinkingsquare(150 - i * 20)


# Closes The Turtle
turtle.done()
