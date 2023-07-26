from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Down(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-40, 250)

    def show_number(self, n):
        self.clear()
        self.color("green")
        self.write(f"Invader Down: {n}/5", align="left", font=FONT)
