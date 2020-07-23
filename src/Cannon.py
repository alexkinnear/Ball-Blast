import pygame


class Cannon:
    def __init__(self, x, y, width, height, vel, fire_rate, fire_power):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.fire_rate = fire_rate
        self.fire_power = fire_power

    def create(self, dis, x, y, width, height):
        image = pygame.image.load("imgs/cannon.png")
        cannon = pygame.transform.scale(image, (width, height))
        dis.blit(cannon, (x, y))

    def move(self, x, width, dis_width, vel):
        key_input = pygame.key.get_pressed()
        # move left
        if x >= 0:
            if key_input[pygame.K_LEFT]:
                x -= vel
        # move right
        if x + width <= dis_width:
            if key_input[pygame.K_RIGHT]:
                x += vel


