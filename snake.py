from turtle import Screen,Turtle
tim=Turtle()
screen=Screen()
up=90
down=270
left=180
right=0
class Snake:
    def __init__(self):
        self.a = 0
        self.segments = []
        self.create_snake()
    def create_snake(self):
        screen.tracer(0)
        a=0
        for position in range(3):
            self.add_segment(position)
    def add_segment(self,position):
        a=0
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(20 - a, 0)
        a = 20 + a
        self.segments.append(tim)


    def extend(self):
        self.add_segment(self.segments[-1].position())
        # add a new segment
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(20)
    def up(self):
        if (self.segments[0].heading() !=down):
            self.segments[0].setheading(90)
    def down(self):
        if (self.segments[0].heading() != up):
            self.segments[0].setheading(270)
    def left(self):
        if (self.segments[0].heading() != right):
            self.segments[0].setheading(180)
    def right(self):
        if (self.segments[0].heading() != left):
            self.segments[0].setheading(0)
        # return self.segments[0].fd(20),self.segments[0].left(90)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]