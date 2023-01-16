import pygame
from Menu import Menu
from game_over import Game_over
from player import Player

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400 # разрешение экрана
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        # отрисовка и изменение свойств объектов

        pygame.display.flip()
    pygame.quit()