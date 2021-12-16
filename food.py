from turtle import Turtle
from random import randint


class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(20 * (randint(-13, 13)), 20 * (randint(-13, 13)))
