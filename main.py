from turtle import Turtle, Screen
import time
from random import randint

WIDTH = 600
HEIGHT = 600
SPEED = 20
screen = Screen()
screen.title("Snake Game")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
snakes = []


def setup_score_turtle():
    turtle = Turtle()
    turtle.hideturtle()
    turtle.pencolor("white")
    turtle.penup()
    turtle.speed(0)
    return turtle


def increase_score():
    global score
    score += 10
    print_score(score_writer, score)


def print_score(score_writer, score):
    score_writer.clear()
    score_writer.goto(0, HEIGHT / 2 - 30)
    score_writer.write(f"Score = {score}", move=False, align='center', font=('Arial', 10, 'normal'))


score: int = 0
score_writer = setup_score_turtle()
print_score(score_writer, score)
snake_coordinates = [(0, 0)]



def add_snake():
    snake = Turtle()
    snake.color("white")
    snake.shape("square")
    snake.penup()
    snake.speed(0)
    snakes.append(snake)
    snake_coordinates.append((snake_coordinates[-1][0]-20, 0))

def update_coordinates():
    snake_coordinates.insert(0, snakes[0].position())
    snake_coordinates.pop()


def line_up_snake():
    for i in range(len(snakes)):
        snakes[i].goto(snake_coordinates[i])

def move(snakes):
    for snake in snakes:
        snake.forward(SPEED)

def move_up():
    snakes[0].setheading(90)

def move_down():
    snakes[0].setheading(270)

def move_left():
    snakes[0].setheading(180)

def move_right():
    snakes[0].setheading(0)

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()

for _ in range(3):
    add_snake()
line_up_snake()


food = Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(20*(randint(-14, 14)), 20*(randint(-14, 14)))

def add_food():
    if not food.isvisible():
        food.goto(20*(randint(-14, 14)), 20*(randint(-14, 14)))
        food.showturtle()

def eat_food():
    if round(snakes[0].xcor()) == round(food.xcor()) and round(snakes[0].ycor()) == round(food.ycor()):
        food.hideturtle()
        increase_score()
        add_snake()
        line_up_snake()

#TODO 0: Refactor the code as per OOPs

#TODO 1: Add boundries and collision with boundries

#TODO 2: Add collision with self

while True:
    snakes[0].forward(SPEED)
    update_coordinates()
    line_up_snake()
    eat_food()
    add_food()
    screen.update()
    time.sleep(.1)



screen.exitonclick()
