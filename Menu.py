# Здесь опишем класс меню
# обязательный метод update()
import pygame
import os
import sys

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        '''Заставка появляется, играет музыка, появляется фон'''
        pass

    def start_screen():
        intro_text = ["ЗАСТАВКА", "",
                      "Правила игры",
                      "Если в правилах несколько строк,",
                      "приходится выводить их построчно"]

        fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return  # начинаем игру

            pygame.display.flip()
            clock.tick(FPS)



    def update(self):
        pass

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Перемещение героя')
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    tile_width = 50
    tile_height = 50
    FPS = 50