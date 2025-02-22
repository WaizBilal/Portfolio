from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
score = ScoreBoard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #collision with food
    if snake.head.distance(food)< 18:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()

    for box in snake.boxes[1:]:
        if snake.head.distance(box) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()


