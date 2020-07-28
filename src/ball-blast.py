import pygame

from Cannon import Cannon
from Ball import Ball
from Rock import Rock

pygame.init()

# ------ Display ------
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Ball Blast")
dis.fill((255, 255, 255))

clock = pygame.time.Clock()
fps = 360

# ------ Background ------
img = pygame.image.load("imgs/background.jpg")
background = pygame.transform.scale(img, (dis_width, dis_height))
dis.blit(background, (0, 0))

# ------ Cannon ------
cannon = Cannon(340, 500, 100, 100, 25, 5, 2)
cannon.create(dis)

# ------Cannon Ball ------
cannon_ball = Ball(cannon.x + cannon.width / 7, cannon.y - cannon.height / 7, 70, 40, 30)
balls = []

# ------ Rock ------
rock = Rock(100, 100, 100, 5, 20, 'DOWN')
rocks = []


def gameLoop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        cannon.move(cannon, dis_width)
        dis.blit(background, (0, 0))
        cannon.create(dis)
        cannon_ball.create(cannon.x + cannon.width / 7, cannon.y - cannon.height / 7, cannon_ball.width,
                         cannon_ball.height, cannon_ball.vel, balls)
        cannon_ball.show(dis, cannon_ball.width, cannon_ball.height, balls)
        rock.hit(balls, rocks, cannon.fire_power)
        rock.create(rocks, dis_width)
        rock.draw(dis, rocks)
        rock.movement(dis_width, dis_height, rocks)
        pygame.display.update()
        clock.tick(fps)


gameLoop()

pygame.quit()
