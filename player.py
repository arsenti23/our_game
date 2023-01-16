# Здесь опишем класс игрока
# обязательный метод update()
import pygame
from Menu import Menu

class Tile(pygame.sprite.Sprite, Menu):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(self.tiles_group, self.all_sprites)
        self.image = self.tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

class Player(pygame.sprite.Sprite, Menu):
    def __init__(self, pos_x, pos_y):
        super().__init__(self.player_group, self.all_sprites)
        self.pos = tile_width * pos_x + 15, tile_height * pos_y + 5
        self.image = self.player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def update(self, x, y):
        pos_x, pos_y = x, y
        self.pos = tile_width * pos_x + 15, tile_height * pos_y + 5
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

tile_width = 50
tile_height = 50