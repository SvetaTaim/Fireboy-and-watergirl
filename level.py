import pygame
from const import *
from characters import Tiles, Crystal, Door, Pond
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
    def __init__(self, change_level):
        filename = f"map{change_level}.txt"
        self.background = load_image('background.png')
        self.tile = load_image('wall.png')
        self.map = open(f"data/{filename}").readlines()
        self.name = change_level

    def render(self, screen, tiles, fire_crystal, water_crystal, boy_door, girl_door, water_ponds, fire_ponds):
        screen.fill((0, 0, 0))
        for y in range(len(self.map)):
            for x in range(len(self.map[0]) - 1):
                if self.map[y][x] == '&':
                    boy_coor = x * TILE_SIZE, y * TILE_SIZE
                elif self.map[y][x] == '@':
                    girl_coor = x * TILE_SIZE, y * TILE_SIZE
                if self.map[y][x] in '#fw':
                    tile = Tiles(x * TILE_SIZE, y * TILE_SIZE)
                    tiles.add(tile)
                    if self.map[y][x] == 'f':
                        pond = Pond(x * TILE_SIZE, y * TILE_SIZE - 3, 'fire')
                        fire_ponds.add(pond)
                    if self.map[y][x] == 'w':
                        pond = Pond(x * TILE_SIZE, y * TILE_SIZE - 3, 'water')
                        water_ponds.add(pond)
                elif self.map[y][x] == '!':
                    door = Door(x * TILE_SIZE, (y + 1) * TILE_SIZE - DOOR_SIZE[1], 'fire')
                    boy_door.add(door)
                elif self.map[y][x] == '?':
                    door = Door(x * TILE_SIZE, (y + 1) * TILE_SIZE - DOOR_SIZE[1], 'water')
                    girl_door.add(door)
                else:
                    screen.blit(pygame.transform.scale(self.background, (TILE_SIZE, TILE_SIZE)), (x * TILE_SIZE, y * TILE_SIZE))
                if self.map[y][x] == '1':
                    crystal = Crystal(x * TILE_SIZE, y * TILE_SIZE, 'fire')
                    fire_crystal.add(crystal)
                if self.map[y][x] == '2':
                    crystal = Crystal(x * TILE_SIZE, y * TILE_SIZE, 'water')
                    water_crystal.add(crystal)
        return (boy_coor, girl_coor)

    def level(self):
        return self.name


    def get_tile_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]
