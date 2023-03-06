import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Game_over(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        '''Заставка появляется, появляется фон'''
        pygame.init()

        self.size = self.width, self.height = 600, 300
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Tank. Game over')
        self.start_screen()
        self.update()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def start_screen(self):
        fon = pygame.transform.scale(load_image('gameover.png'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))

    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
            pygame.display.flip()

