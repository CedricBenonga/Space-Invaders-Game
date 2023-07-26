from turtle import Turtle

FONT = ("Courier", 22, "bold")


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("blue")
        self.penup()

    def warning(self, n):
        self.goto(0, 0)
        self.clear()
        self.write(f"Level: {n}", align="center", font=FONT)

    def game_on(self):
        self.clear()

    def game_over(self, n):
        self.goto(0, 0)
        self.clear()
        self.color("green")
        self.write(f"{n}", align="center", font=FONT)

