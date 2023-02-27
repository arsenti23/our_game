import pygame
import os
import sys



pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
running = True
color1 = (0, 0, 0)
color2 = (255, 255, 255)
color3 = (255, 0, 0)
color4 = (0, 255, 0)
color5 = (0, 0, 255)
FPS = 30

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 50))
        self.image.fill(color5)
        self.rect = self.image.get_rect()
        self.rect.center = (0, height // 2)

    def update(self):
        pass

def terminate(self):
    pygame.quit()
    sys.exit()

my_sprites = pygame.sprite.Group()
player = Player()
my_sprites.add(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    screen.fill(color1)
    my_sprites.draw(screen)
    pygame.display.flip()
