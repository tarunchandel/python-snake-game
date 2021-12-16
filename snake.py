from turtle import Turtle

SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
WIDTH = 600
HEIGHT = 600


class Snake:
    def __init__(self):
        self.snake_pieces = []
        self.snake_coordinates = []
        self.setup_snake()

    def add_snake_piece(self):
        snake_piece = Turtle()
        snake_piece.speed(0)
        snake_piece.penup()
        snake_piece.color("white")
        snake_piece.shape("square")
        self.snake_pieces.append(snake_piece)
        self.snake_coordinates.append((self.snake_coordinates[-1][0] - 20, 0))

    def update_coordinates(self):
        self.snake_coordinates.insert(0, (round(self.snake_head.xcor()), round(self.snake_head.ycor())))
        self.snake_coordinates.pop()

    def line_up_snake(self):
        for i in range(len(self.snake_pieces)):
            self.snake_pieces[i].goto(self.snake_coordinates[i])

    def move(self):
        self.snake_head.forward(SPEED)
        self.update_coordinates()
        self.line_up_snake()
        return self.detect_collision()

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def self_collision(self):
        if self.snake_head.position() in self.snake_coordinates[1:]:
            return True
        else:
            return False

    def wall_collision(self):
        if self.snake_head.xcor() >= WIDTH / 2 - 20 \
                or self.snake_head.xcor() <= -WIDTH / 2 + 10 \
                or self.snake_head.ycor() >= HEIGHT / 2 - 10 \
                or self.snake_head.ycor() <= -HEIGHT / 2 + 20:
            return True
        else:
            return False

    def detect_collision(self):
        if self.wall_collision() or self.self_collision():
            self.snake_head.color("red")
            return False
        else:
            return True

    def restart(self):
        for snake in self.snake_pieces:
            snake.hideturtle()
        del self.snake_pieces[:]
        del self.snake_coordinates[:]

        self.setup_snake()

    def setup_snake(self):
        self.snake_coordinates = [(0, 0)]
        for _ in range(3):
            self.add_snake_piece()
        self.line_up_snake()
        self.snake_head = self.snake_pieces[0]
