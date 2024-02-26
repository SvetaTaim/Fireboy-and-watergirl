import pygame
from const import *
from characters import Tiles, Crystal
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
        self.boy_door = load_image('boy_door.png')
        self.girl_door = load_image('girl_door.png')
        self.map = open(f"data/{filename}").readlines()
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

    def render(self, screen, tiles, fire_crystal, water_crystal):
        for y in range(len(self.map)):
            for x in range(len(self.map[0]) - 1):
                if self.map[y][x] == '&':
                    boy_coor = x * TILE_SIZE, y * TILE_SIZE
                elif self.map[y][x] == '@':
                    girl_coor = x * TILE_SIZE, y * TILE_SIZE
                if self.map[y][x] == '#':
                    tile = Tiles(x * TILE_SIZE, y * TILE_SIZE)
                    tiles.add(tile)
                elif self.map[y][x] == '!':
                    screen.blit(pygame.transform.scale(self.boy_door, (TILE_SIZE, TILE_SIZE)), (x * TILE_SIZE, y * TILE_SIZE))
                elif self.map[y][x] == '?':
                    screen.blit(pygame.transform.scale(self.girl_door, (TILE_SIZE, TILE_SIZE)), (x * TILE_SIZE, y * TILE_SIZE))
                else:
                    screen.blit(pygame.transform.scale(self.background, (TILE_SIZE, TILE_SIZE)), (x * TILE_SIZE, y * TILE_SIZE))
                if self.map[y][x] == '1':
                    crystal = Crystal(x * TILE_SIZE, y * TILE_SIZE, 'fire')
                    fire_crystal.add(crystal)
                if self.map[y][x] == '2':
                    crystal = Crystal(x * TILE_SIZE, y * TILE_SIZE, 'water')
                    water_crystal.add(crystal)
        return (boy_coor, girl_coor)


    def get_tile_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]
