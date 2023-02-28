import pygame
import os
import sys
import random
from menu import Menu
from game_over import Game_over

pygame.init()
size = width, height = 600, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tank")
running = True
clock = pygame.time.Clock()
FPS = 120
color1 = (0, 0, 0)
color2 = (255, 255, 255)
color3 = (255, 0, 0)
color4 = (0, 255, 0)
color5 = (0, 0, 255)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def draw(screen, number):
    font = pygame.font.Font(None, 30)
    text = font.render(f"Счет: {number}", True, (100, 255, 100))
    screen.blit(text, (10, 10))


class Player(pygame.sprite.Sprite):  # игрок
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.w, self.h = 70, 70
        self.imag = load_image("tank.png")
        self.image = pygame.transform.scale(self.imag, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.x, self.y = width // 2, height - 40
        self.rect.center = self.x, self.y
        self.playerx = 0

    def update(self):
        self.playerx = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
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


class Missile(pygame.sprite.Sprite):  # снаряд
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


class Bomb(pygame.sprite.Sprite):  # бомбы
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


class Bomb_boom(pygame.sprite.Sprite):
    def __init__(self, r_center):
        pygame.sprite.Sprite.__init__(self)
        self.image_boom = load_image("boom.png")
        self.image = self.image_boom
        self.rect = self.image.get_rect()
        self.rect.center = r_center
        self.time1 = pygame.time.get_ticks()

    def update(self):
        self.time_boom = 1000
        self.time2 = pygame.time.get_ticks()
        print(2, self.time2)
        if self.time2 - self.time1 >= self.time_boom:
            self.time1 = self.time2
            self.kill()
        r_center = self.rect.center
        self.image = self.image_boom
        self.rect = self.image.get_rect()
        self.rect.center = r_center


all_sprites = pygame.sprite.Group()
bombs = pygame.sprite.Group()
missiles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(7):
    bomb = Bomb()
    all_sprites.add(bomb)
    bombs.add(bomb)

score = 0

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.missile()

    collides = pygame.sprite.spritecollide(player, bombs, False)  # столкновения бомбы и игрока
    if collides:
        gm = Game_over(True)
        gm.update()
        running = False

    collides = pygame.sprite.groupcollide(bombs, missiles, True, True)
    for i in collides:
        score += 1
        bm = Bomb_boom(i.rect.center)
        all_sprites.add(bm)
        bomb = Bomb()
        all_sprites.add(bomb)
        bombs.add(bomb)
    pygame.display.update()
    all_sprites.update()
    screen.fill(color1)
    draw(screen, str(score))
    all_sprites.draw(screen)
    pygame.display.flip()

f = open("data/score.txt", 'a')
print(str(score), file=f)
f.close()
pygame.quit()
