from turtle import Turtle


class Score(Turtle):
    def __init__(self, height):
        super().__init__()
        self.HEIGHT = height
        self.score: int = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.speed(0)
        self.print_score()

    def increase_score(self):
        self.score += 10
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(0, self.HEIGHT / 2 - 30)
        self.write(f"Score = {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def restart(self):
        self.score = 0
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\nClick to restart.", move=False, align='center', font=('Arial', 20, 'normal'))
