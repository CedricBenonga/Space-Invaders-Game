import random
from turtle import Turtle
from level import Level

STARTING_MOVE_DISTANCE = 50
MOVE_INCREMENT = 25


class Invaders:

    def __init__(self):
        self.all_invaders = []
        self.invader_speed = STARTING_MOVE_DISTANCE
        self.loading = Level()

    def create_invader(self):
        random_selector = random.randint(1, 2)
        if random_selector == 1:
            new_invader = Turtle("triangle")
            new_invader.hideturtle()
            new_invader.shapesize(stretch_wid=2, stretch_len=3)
            new_invader.penup()
            new_invader.color("purple")
            new_invader.right(90)
            random_x = random.randrange(-270, 270, 45)
            new_invader.goto(random_x, 290)
            new_invader.showturtle()
            self.all_invaders.append(new_invader)

    def move_invaders(self):
        for invader in self.all_invaders:
            invader.forward(self.invader_speed)

    def level_up(self):
        self.invader_speed += MOVE_INCREMENT

    def game_over(self):
        for invader in self.all_invaders:
            invader.goto(1000, 1000)


