import pygame
from Menu import Menu
from game_over import Game_over
from player import Player
from media import Media

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400 # разрешение экрана
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()