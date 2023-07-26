from turtle import Turtle


class Invader_Shooting:

    def __init__(self):
        self.i_gun = []
        self.shot_speed = 100

    def load_gun(self, invader_x, invader_y):
        if True:
            i_bullet = Turtle("triangle")
            i_bullet.hideturtle()
            i_bullet.shapesize(stretch_wid=0.5, stretch_len=.5)
            i_bullet.penup()
            i_bullet.color("red")
            i_bullet.right(90)
            i_bullet.goto(invader_x, invader_y)
            i_bullet.showturtle()
            self.i_gun.append(i_bullet)

    def shoot(self):
        for shot in self.i_gun:
            shot.forward(self.shot_speed)

    def game_over(self):
        for shot in self.i_gun:
            shot.goto(1000, 1000)
