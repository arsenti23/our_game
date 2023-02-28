import pygame
import os
import sys
import random

pygame.init()
size = width, height = 600, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()
running = True
color1 = (0, 0, 0)
color2 = (255, 255, 255)
color3 = (255, 0, 0)
color4 = (0, 255, 0)
color5 = (0, 0, 255)
FPS = 120


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.w, self.h = 70, 70
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(color5)
        self.rect = self.image.get_rect()
        self.x, self.y = width // 2, height - 40
        self.rect.center = self.x, self.y
        self.playerx = 0

    def update(self):
        self.playerx = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print(3)
                self.playerx = -1
            if event.key == pygame.K_RIGHT:
                self.playerx = 1
        self.rect.x += self.playerx
        if self.rect.right > width:
            print(4)
            self.rect.right = 0 + self.w
        elif self.rect.left < 0:
            self.rect.left = width - self.w

    def missile(self):
        missile = Missile(self.rect.center, self.rect.top)
        all_sprites.add(missile)
        missiles.add(missile)


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.w, self.h = 30, 30
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(color3)
        self.rect = self.image.get_rect()
        self.create()

    def update(self):
        self.rect.y += self.bomb_coord_y
        if self.rect.y > height + 10:
            self.create()

    def create(self):
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-200, -30)
        self.bomb_coord_y = random.randrange(1, 4)


class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.w, self.h = 5, 20
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(color4)
        self.rect = self.image.get_rect()
        self.rect.center = x
        self.rect.bottom = y

        self.coordy = -10

    def update(self):
        self.rect.y += self.coordy
        if self.rect.bottom < 0:
            self.kill()


def terminate(self):
    pygame.quit()
    sys.exit()


all_sprites = pygame.sprite.Group()
bombs = pygame.sprite.Group()
missiles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(7):
    bomb = Bomb()
    all_sprites.add(bomb)
    bombs.add(bomb)

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.missile()
    all_sprites.update()
    screen.fill(color1)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
