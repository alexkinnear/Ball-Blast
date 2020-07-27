import pygame


class Rock:
    def __init__(self, x, y, width, vel, health):
        self.x = x
        self.y = y
        self.width = width
        self.vel = vel
        self.health = health

    def draw(self, dis):
        self.y += self.vel
        image = pygame.image.load("imgs/rock.png")
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(str(self.health), True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.x/2, self.y/2)
        rock = pygame.transform.scale(image, (self.width, self.width))
        rock.blit(text, text_rect)
        dis.blit(rock, (self.x, self.y))
