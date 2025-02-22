import turtle

paddle = turtle
class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
    def go_up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(),new_y)

