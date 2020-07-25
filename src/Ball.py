import pygame


class Ball:
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def create(self, dis, x, y, width, height, vel):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            image = pygame.image.load("imgs/cannon-ball.png")
            cannon_ball = pygame.transform.scale(image, (width, height))
            y -= vel
            dis.blit(cannon_ball, (x, y))

