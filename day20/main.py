from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Saga")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.update_score()
        food.refresh()
    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.reset()
        scoreboard.game_over()

    # Detect collision with tail
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 10:
            game_on = False
            scoreboard.reset()
            scoreboard.game_over()

screen.exitonclick()
