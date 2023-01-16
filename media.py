import pygame


class Media:
    def load_level(self, filename):
        filename = 'data/' + self.filename
        with open(filename, 'r') as mapFile:
            self.level_map = [line.strip() for line in mapFile]
        max_width = max(map(len, self.level_map))
        return list(map(lambda x: x.ljust(max_width, '.'), self.level_map))

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', self.name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    def generate_level(self, level):
        new_player, x, y = None, None, None
        for y in range(len(self.level)):
            for x in range(len(self.level[y])):
                if self.level[y][x] == '.':
                    Tile('empty', x, y)
                elif self.level[y][x] == '#':
                    Tile('wall', x, y)
                elif self.level[y][x] == '@':
                    Tile('empty', x, y)
                    new_player = Player(x, y)
        return new_player, x, y

med = Media()