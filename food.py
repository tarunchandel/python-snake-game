from turtle import Turtle
from random import randint


class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.shape("circle")
        self.food.color("green")
        self.food.penup()
        self.food.goto(20 * (randint(-14, 14)), 20 * (randint(-14, 14)))

    def add_food(self):
        if not self.food.isvisible():
            self.food.goto(20 * (randint(-14, 14)), 20 * (randint(-14, 14)))
            self.food.showturtle()

    def eat_food(self, snake, score):
        if round(snake.snake_head.xcor()) == round(self.food.xcor()) \
                and round(snake.snake_head.ycor()) == round(self.food.ycor()):
            self.food.hideturtle()
            score.increase_score()
            snake.add_snake_piece()
            snake.line_up_snake()
            self.add_food()

