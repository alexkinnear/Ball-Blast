import pygame


class Ball:
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def create(self, x, y, width, height, vel, balls):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            ball = Ball(x, y, width, height, vel)
            balls.append(ball)

    def show(self, dis, width, height, balls):
        image = pygame.image.load("imgs/cannon-ball.png")
        for cb in balls:
            cb.y -= cb.vel
            cannon_ball = pygame.transform.scale(image, (width, height))
            dis.blit(cannon_ball, (cb.x, cb.y))
