from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('triangle')
        self.color("green")
        self.left(90)
        self.shapesize(stretch_wid=2, stretch_len=3)
        self.shapetransform()
        self.penup()
        self.goto(0, -250)
        self.showturtle()

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def game_over(self):
        self.goto(1000, 1000)
