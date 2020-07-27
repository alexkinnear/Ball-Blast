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

    def create(self, dis):
        image = pygame.image.load("imgs/cannon.png")
        cannon = pygame.transform.scale(image, (self.width, self.height))
        dis.blit(cannon, (self.x, self.y))

    def move(self, cannon, dis_width):
        keys_pressed = pygame.key.get_pressed()
        if cannon.x > 0:
            if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
                cannon.x -= cannon.vel
        if cannon.x + cannon.width < dis_width:
            if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
                cannon.x += cannon.vel
        pygame.display.update()




