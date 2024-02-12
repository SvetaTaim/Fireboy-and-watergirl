import pygame
from const import *
import sys
import os

def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

class Fireboy_and_Watergirl:
    def __init__(self, filename, free_tiles, finish_tile):
        self.background = load_image('background.png')
        self.tile = load_image('wall.png')
        self.map = open(f"data/{filename}").readlines()
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

    def render(self, screen):
        for y in range(WINDOW_HEIGHT // TILE_SIZE):
            for x in range(WINDOW_WIDTH // TILE_SIZE):
                if self.map[y][x] == '#':
                    screen.blit(self.tile, (x * TILE_SIZE, y * TILE_SIZE))
                else:
                    screen.blit(self.background, (x * TILE_SIZE, y * TILE_SIZE))


    def get_tile_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]
