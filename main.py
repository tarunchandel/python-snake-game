from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.title("Snake Game")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score(HEIGHT)

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_on = True
while game_on:
    game_on = snake.move()
    food.eat_food(snake, score)
    screen.update()
    time.sleep(.1)

screen.exitonclick()
