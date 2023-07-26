from turtle import Turtle


class Player_Shooting:

    def __init__(self):
        self.gun = []
        self.bullet_speed = 100

    def load_gun(self, gun_x, gun_y):
        if True:
            bullet = Turtle("triangle")
            bullet.hideturtle()
            bullet.shapesize(stretch_wid=0.5, stretch_len=.5)
            bullet.penup()
            bullet.color("blue")
            bullet.left(90)
            bullet.goto(gun_x, gun_y)
            bullet.showturtle()
            self.gun.append(bullet)

    def shoot(self):
        for shot in self.gun:
            shot.forward(self.bullet_speed)

    def game_over(self):
        for shot in self.gun:
            shot.goto(1000, 1000)


