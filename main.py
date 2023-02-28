import pygame
import os
import sys
import random
from game_over import Game_over


pygame.init()
size = width, height = 600, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shooter")
running = True
color1 = (0, 0, 0)
color2 = (255, 255, 255)
color3 = (255, 0, 0)
color4 = (0, 255, 0)
color5 = (0, 0, 255)
clock = pygame.time.Clock()
FPS = 120
all_sprites = pygame.sprite.Group()
bombs = pygame.sprite.Group()
missiles = pygame.sprite.Group()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


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


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb2.png")
    image_boom = load_image("boom.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.imag = Bomb.image
        self.image = pygame.transform.scale(self.imag, (50, 50))
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

    def boom(self):
        self.image = self.image_boom



def terminate(self):
    pygame.quit()
    sys.exit()



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

    collides = pygame.sprite.groupcollide(bombs, missiles, True, True)
    for i in collides:
        bomb = Bomb()
        all_sprites.add(bomb)
        bombs.add(bomb)

    collides = pygame.sprite.spritecollide(player, bombs, False)
    if collides:
        running = False
        gm = Game_over()

    all_sprites.update()
    screen.fill(color1)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
