import pygame
import random


class Rock:
    def __init__(self, x, y, width, vel, health):
        self.x = x
        self.y = y
        self.width = width
        self.vel = vel
        self.health = health

    def create(self, rocks, dis_width):
        if len(rocks) < 2:
            rock = Rock(random.randint(0, dis_width - self.width), random.randint(0, 50), 100, random.randrange(5, 10, 5),
                        random.randint(20, 30))
            rocks.append(rock)

    def draw(self, dis, rocks):
        image = pygame.image.load("imgs/rock.png")
        font = pygame.font.Font('freesansbold.ttf', 32)

        for i, rock in enumerate(rocks):
            text = font.render(str(rock.health), True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (rock.x / 2, rock.y / 2)
            rock1 = pygame.transform.scale(image, (rock.width, rock.width))
            dis.blit(rock1, (rock.x, rock.y))
            dis.blit(text, (rock.x + rock.width/3, rock.y + rock.width/3))
            rock.y += rock.vel

    def hit(self, balls, rocks):
        for i, rock in enumerate(rocks):
            for j, ball in enumerate(balls):
                if ball.x + ball.width > rock.x and ball.x < rock.x + rock.width \
                        and ball.y < rock.y + rock.width:
                    rock.health -= 1
                    balls.pop(j)
            if rock.health < 1:
                rocks.pop(i)
