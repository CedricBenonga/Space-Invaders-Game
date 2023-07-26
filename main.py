import time
from turtle import Screen
from down import Down
from player import Player
from invaders import Invaders
from player_shooting import Player_Shooting
from level import Level
from scoreboard import Scoreboard
from invader_shooting import Invader_Shooting

# Screen set up
screen = Screen()
screen.title("@ Cedric Benonga")
screen.setup(width=600, height=600)
screen.bgpic('img/bg_img.png')

# Introducing all the OOPs
player = Player()
p_shooting = Player_Shooting()
invaders = Invaders()
i_shooting = Invader_Shooting()
scoreboard = Scoreboard()

level = Level()
level_nbr = 1
level.warning(level_nbr)

level_checker = []
down = Down()
down.show_number(len(level_checker))

# Moving the player's ship in 4 directions
screen.listen()
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")


game_is_on = True

while game_is_on:
    time.sleep(0.001)
    screen.update()

    # Loading invaders
    invaders.create_invader()
    # Moving invaders
    invaders.move_invaders()

    # Loading user's gun
    p_shooting.load_gun(player.xcor(), player.ycor())
    # Shooting invaders
    p_shooting.shoot()

    level.game_on()

    for invader in invaders.all_invaders:

        # Loading invader's gun
        i_shooting.load_gun(invader.xcor(), invader.ycor())
        # Shooting the user's ship
        i_shooting.shoot()

        # Loading user's gun
        p_shooting.load_gun(player.xcor(), player.ycor())
        # Shooting invaders
        p_shooting.shoot()

        # Removing the destroyed invader and the used bullet
        for bullet in p_shooting.gun:
            if bullet.distance(invader) <= 60:

                # Explode and remove the rocket on a Successful shot to invader
                bullet.color("red")
                bullet.shape("circle")
                bullet.shapesize(stretch_wid=4, stretch_len=4)
                bullet.hideturtle()
                bullet.goto(1000, 1000)

                # Invader's ship explosion
                invader.color("red")
                invader.shape("circle")
                invader.shapesize(stretch_wid=10, stretch_len=10)
                invader.hideturtle()
                invader.goto(1000, 1000)
                level_checker.append(invader)
                down.show_number(len(level_checker))

                # handling occasional errors
                try:
                    invaders.all_invaders.remove(invader)
                except ValueError:
                    pass

            # Changing level, increase invaders speed and update the scoreboard
            if len(level_checker) == 5:
                level_nbr += 1
                level_checker.clear()

                screen.clear()
                screen.bgpic('img/bg_img.png')
                player = Player()

                screen.listen()
                screen.onkey(player.go_right, "Right")
                screen.onkey(player.go_left, "Left")
                screen.onkey(player.go_up, "Up")
                screen.onkey(player.go_down, "Down")

                scoreboard.increase_level()
                down.show_number(len(level_checker))
                invaders.level_up()
                level.warning(level_nbr)

            # End the game if the player's ship bumps the invaders one or if an invader managed to pass through
            if invader.distance(player) <= 100 or invader.ycor() <= -200:

                # Player's ship explosion on collusion with an invader ship
                if invader.distance(player) <= 100:
                    player.color("red")
                    player.shape("circle")
                    player.shapesize(stretch_wid=10, stretch_len=10)

                # Screen clear up
                screen.clear()

                # Game over reason
                if invader.distance(player) <= 100:
                    level.game_over('Collusion with an invader ship')
                if invader.ycor() <= -220:
                    level.game_over('An invader managed to pass through!')

                # Screen update
                screen.bgpic('img/bg_img.png')
                scoreboard.game_over()
                i_shooting.game_over()
                invaders.game_over()
                p_shooting.game_over()
                player.game_over()

                # Stop game
                game_is_on = False
                break

        # On invaders successful shot to the user's ship
        for i_bullet in i_shooting.i_gun:
            if i_bullet.distance(player) <= 35:

                # User's ship explosion
                player.color("red")
                player.shape("circle")
                player.shapesize(stretch_wid=10, stretch_len=10)

                # Screen clear up
                screen.clear()

                # Game over reason
                level.game_over('Invaders did shoot you down!')

                # Screen update
                screen.bgpic('img/bg_img.png')
                scoreboard.game_over()
                i_shooting.game_over()
                invaders.game_over()
                p_shooting.game_over()
                player.game_over()

                # Stop game
                game_is_on = False
                break

screen.exitonclick()
