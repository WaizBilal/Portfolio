from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
ball = Ball()
scoreboard = ScoreBoard()

l_paddle= Paddle((-380,0))
r_paddle = Paddle((380,0))

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "z")
game_is_on = True
while game_is_on == True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle)<50 and ball.xcor() < -360:
        ball.bounce_x()
    if ball.xcor() > 400 :
        ball.reset_position()
        scoreboard.lpoint()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.rpoint()





screen.exitonclick()
