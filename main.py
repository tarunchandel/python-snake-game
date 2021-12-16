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


def game_reset():
    snake.restart()
    score.restart()
    food.refresh()
    screen.listen()
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")


screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_on = True
game_continue = True


def go_on(x, y):
    game_reset()
    global game_on
    game_on = True
    screen.onclick(None)
    play_game()


def play_game():
    global game_on
    while game_on:
        game_on = snake.move()
        if snake.snake_head.distance(food) < 20:
            food.refresh()
            score.increase_score()
            snake.add_snake_piece()
            snake.line_up_snake()
        screen.update()
        time.sleep(.1)
        if not game_on:
            score.game_over()
            screen.onclick(go_on)


play_game()
screen.mainloop()
