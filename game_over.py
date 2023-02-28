# Здесь опишем класс конечной заставки
# обязательный метод update()
import pygame

pygame.init()
pygame.display.set_caption('Tank. Game over')
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
running = True

class Game_over(pygame.sprite.Sprite):
    def __init__(self, running):
        self.running = running

    def update(self):

        x, y = -600, 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            if x < 0:
                x += 1
            screen.fill((0, 0, 255))
            cursor = pygame.image.load('data/gameover.png')
            screen.blit(cursor, (x, y))
            pygame.display.flip()

