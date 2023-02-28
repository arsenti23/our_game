# Здесь опишем класс меню
# обязательный метод update()
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


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        '''Заставка появляется, появляется фон'''
        pygame.init()

        self.size = self.width, self.height = 800, 800
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption('Tank')
        self.clock = pygame.time.Clock()
        self.running = True
        self.start_screen()
        self.update()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def start_screen(self):
        intro_text = ["Инструкция.", "Вам дано три пункта:",
                      "Старт - запускается игра.",
                      "Рекорды - лучшие результаты игр.",
                      "Выход - выйти из игры."]
        fon = pygame.transform.scale(load_image('fon2.png'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)
        self.buttons()

    def buttons(self):
        name_buttons = ['Старт', 'Рекорды', 'Выход']
        font = pygame.font.Font(None, 100)
        text_coord = 250
        for name in name_buttons:
            string_rendered = font.render(name, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            print(intro_rect)
            text_coord += 40
            intro_rect.top = text_coord
            intro_rect.x = 250
            text_coord += intro_rect.height
            pygame.draw.rect(self.screen, (0, 0, 255), (intro_rect[0] - 10, intro_rect[1] - 10, intro_rect[2] + 20,
                                                        intro_rect[3] + 20), 4)
            self.screen.blit(string_rendered, intro_rect)

    def update(self):
        while True:
            self.rr = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 245 <= event.pos[0] <= 445 and 285 <= event.pos[1] <= 370:
                        print(event.pos, 1)
                        self.rr = 0


                    elif 245 <= event.pos[0] <= 570 and 390 <= event.pos[1] <= 475:
                        print(2)
                        f = open("data/score.txt", 'r')
                        print(f.read())
                        f.close()
                    elif 245 <= event.pos[0] <= 495 and 495 <= event.pos[1] <= 580:
                        self.terminate()
            pygame.display.flip()



