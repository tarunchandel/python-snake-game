from turtle import Turtle


class Score:
    def __init__(self, height):
        self.HEIGHT = height
        self.score: int = 0
        self.score_writer = Turtle()
        self.score_writer.hideturtle()
        self.score_writer.pencolor("white")
        self.score_writer.penup()
        self.score_writer.speed(0)
        self.print_score()

    def increase_score(self):
        self.score += 10
        self.print_score()

    def print_score(self):
        self.score_writer.clear()
        self.score_writer.goto(0, self.HEIGHT / 2 - 30)
        self.score_writer.write(f"Score = {self.score}", move=False, align='center', font=('Arial', 10, 'normal'))
