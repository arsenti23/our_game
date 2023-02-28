# Здесь опишем класс конечной заставки
# обязательный метод update()
import pygame


class Game_over(pygame.sprite.Sprite):
    pygame.init()
    pygame.display.set_caption('Tank. Game over')
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)
    running = True
    x, y = -600, 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if x < 0:
            x += 1
        screen.fill((0, 0, 255))
        cursor = pygame.image.load('data/gameover.png')
        screen.blit(cursor, (x, y))
        pygame.display.flip()

    def update(self):
        pass
