from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance= 20
Up = 90
Down = 270
Left = 180
Right = 0

class Snake():
    def __init__(self):
        self.boxes = []
        self.create_snake()
        self.head = self.boxes[0]

    def create_snake (self):
        for position in starting_position:
            self.add_box(position)
    def add_box(self, position):
        new_box = Turtle("square")
        new_box.color("white")
        new_box.penup()
        new_box.goto(position)
        self.boxes.append(new_box)
    def reset(self):
        for box in self.boxes:
            box.goto(2000,2000)
        self.boxes.clear()
        self.create_snake()
        self.head = self.boxes[0]
    def extend(self):
        self.add_box(self.boxes[-1].position())
    def move(self):
        for i in range(len(self.boxes)-1, 0, -1):
            new_x = self.boxes[i-1].xcor()
            new_y = self.boxes[i-1].ycor()
            self.boxes[i].goto(new_x,new_y)
        self.head.forward(move_distance)
    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)
    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)
    def left(self):
        if self.head.heading() != Right:
            self.boxes[0].setheading(Left)
    def right(self):
        if self.head.heading() != Left:
            self.boxes[0].setheading(Right)






