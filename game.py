import pygame
import os
import sys

pygame.init()
size = width, height = 600, 700
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
        self.w, self.h = 70, 70
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(color5)
        self.rect = self.image.get_rect()
        self.x, self.y = width // 2, height - 40
        self.rect.center = self.x, self.y
        self.coordx = 0

    def update(self):
        self.coordx = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.coordx = -1
            if event.key == pygame.K_RIGHT:
                self.coordx = 1
        self.rect.x += self.coordx
        if self.rect.right > width:
            self.rect.right = 0 + self.w
        elif self.rect.left < 0:
            self.rect.left = width - self.w


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.w, self.h = 70, 70
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(color3)
        self.rect = self.image.get_rect()

    def update(self):
        pass


class Missile(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def update(self):
        pass


def terminate(self):
    pygame.quit()
    sys.exit()


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    all_sprites.update()
    screen.fill(color1)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
