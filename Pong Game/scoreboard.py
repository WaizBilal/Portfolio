import turtle
class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()
    def update(self):
        self.clear()
        self.goto(-100,180)
        self.write(self.l_score,align="center", font= ("Courier",88,"normal"))
        self.goto(100,180)
        self.write(self.r_score,align="center", font= ("Courier",88,"normal"))
    def lpoint(self):
        self.l_score += 1
        self.update()
    def rpoint(self):
        self.r_score += 1
        self.update()
