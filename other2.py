import os
import sys
import pygame
import time


def load_level(filename):
    filename = 'data/' + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.pos = tile_width * pos_x + 15, tile_height * pos_y + 5
        print(self.pos)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def update(self, x, y):
        print(x, y)
        pos_x, pos_y = x, y
        self.pos = tile_width * pos_x + 15, tile_height * pos_y + 5
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


def move(player, vector):
    x, y = player.pos
    x, y = x // 50, y // 50
    if vector == 'LEFT' and (level[y][x - 1] == '.' or level[y][x - 1] == '@'):
        player.update(x - 1, y)
        if x - 1 == 0:
            end_screen()
    elif vector == 'RIGHT' and (level[y][x + 1] == '.' or level[y][x + 1] == '@'):
        player.update(x + 1, y)
        if x + 1 == 15:
            end_screen()
    elif vector == 'UP' and (level[y - 1][x] == '.' or level[y - 1][x] == '@'):
        player.update(x, y - 1)
        if y - 1 == 0:
            end_screen()
    elif vector == 'DOWN' and (level[y + 1][x] == '.' or level[y + 1][x] == '@'):
        player.update(x, y + 1)
        if y + 1 == 15:
            end_screen()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["                                                       ИГРА",
                  "                                                  ЛАБИРИНТ",
                  "",
                  "",
                  "",
                  "",
                  "                                                      Играть",
                  "                                                      Выход"]

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if 335 < event.pos[0] < 400 and 240 < event.pos[1] < 255:
                    tm1 = time.perf_counter()
                    return tm1
                if 335 < event.pos[0] < 400 and 270 < event.pos[1] < 290:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)

def end_screen():
    tm2 = time.perf_counter()
    intro_text = ["",
                  "                                                     ПОБЕДА",
                  "                                                Ваш результат:",
                  f"                                                   {round(tm2 - tm1)} секунд(ы)",
                  "",
                  "",
                  "",
                  "                                                      ВЫЙТИ"]

    fon = pygame.transform.scale(load_image('end_fon.png'), (width, height))
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if 335 < event.pos[0] < 400 and 240 < event.pos[1] < 255:
                    return
                if 335 < event.pos[0] < 400 and 270 < event.pos[1] < 290:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


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
    tm = 0

    player_image = load_image('mar.png')
    tile_images = {
        'wall': load_image('box.png'),
        'empty': load_image('grass.png')
    }

    level = load_level('level_1.txt')
    player, level_x, level_y = generate_level(level)
    tm1 = start_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('LEFT')
                    move(player, 'LEFT')

                if event.key == pygame.K_RIGHT:
                    print('RIGHT')
                    move(player, 'RIGHT')

                if event.key == pygame.K_UP:
                    print('UP')
                    move(player, 'UP')

                if event.key == pygame.K_DOWN:
                    move(player, 'DOWN')
        screen.fill((255, 255, 255))
        tiles_group.draw(screen)
        player_group.draw(screen)
        # изменяем ракурс камеры
        # обновляем положение всех спрайтов
        pygame.display.flip()
        clock.tick(FPS)