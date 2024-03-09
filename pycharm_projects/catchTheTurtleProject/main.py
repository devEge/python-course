import turtle
from random import randint

# Screen Configurations
screen = turtle.Screen()
screen.bgcolor("#212121")
screen.title("Catch the Turtle")

# constants
FONT = ("Verdana", 15, "normal")
SCREEN_HEIGHT = screen.window_height()
SCREEN_WIDTH = screen.window_width()
SCORE = 0
GAME_OVER = False


# score turtle
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()


def setup_countdown_turtle():
    turtle.tracer(0)
    countdown_turtle.hideturtle()
    countdown_turtle.color("#C446E7")
    countdown_turtle.penup()
    top_height = SCREEN_HEIGHT / 2
    countdown_turtle.setpos(0, top_height * 0.84)
    countdown_turtle.write("Time=0", font=FONT, move=False, align="center")
    turtle.tracer(1)


def countdown(time):
    turtle.tracer(0)
    countdown_turtle.clear()
    countdown_turtle.write(f"Time={time}", font=FONT, move=False, align="center")
    turtle.tracer(1)
    if time > 0:
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        global GAME_OVER
        GAME_OVER = True
        countdown_turtle.clear()
        countdown_turtle.write("GAME OVER", font=FONT, move=False, align="center")


def setup_score_turtle():
    turtle.tracer(0)
    score_turtle.hideturtle()
    score_turtle.color("#C446E7")
    score_turtle.penup()
    top_height = SCREEN_HEIGHT / 2
    score_turtle.setpos(0, top_height * 0.9)
    score_turtle.write(f"SCORE={SCORE}", font=FONT, move=False, align="center")
    turtle.tracer(1)


# Main Turtle Configurations
t = turtle.Turtle(shape="turtle")
t.penup()
t.color("green")
t.shapesize(2, 2)


def move_turtle():
    global GAME_OVER
    if not GAME_OVER:
        turtle.tracer(0)
        t.goto(randint(-(SCREEN_WIDTH-30) // 2, (SCREEN_WIDTH-30) // 2), randint(-(SCREEN_HEIGHT-30) // 2, (SCREEN_HEIGHT-30) // 2))
        turtle.tracer(1)
        # recursive function
        screen.ontimer(move_turtle, 600)


def handle_click(x, y):
    global GAME_OVER
    if not GAME_OVER:
        global SCORE
        SCORE += 1
        score_turtle.clear()
        score_turtle.write(f"SCORE={SCORE}", font=FONT, move=False, align="center")


t.onclick(handle_click)


setup_score_turtle()
setup_countdown_turtle()
move_turtle()
countdown(15)


turtle.mainloop()
