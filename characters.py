import pygame
import os
import sys
from const import *

def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    h = 60
    h1 = h / image.get_height()
    w1 = image.get_width() * h1
    image1 = pygame.transform.scale(image, (w1, h))
    image1.set_colorkey((255, 255, 255))
    return image1


class Fireboy(pygame.sprite.Sprite):
    image = load_image("fireboy_stay1.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Fireboy.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.right = False
        self.left = False
        self.jump = False
        self.ground = False
        self.deltax = 0
        self.deltay = 0

    def update(self, tiles):
        if self.right:
            self.deltax += SPEED
        if self.left:
            self.deltax -= SPEED
        if self.jump:
            if self.ground:
                self.deltay -= JUMP
        if not self.ground:
            self.deltay += GRAVITY
        self.rect.x += self.deltax
        self.rect.y += self.deltay
        self.collide(tiles)

    def collide(self, tiles):
        for tile in tiles:
            if pygame.sprite.collide_rect(self, tile):
                if self.right:
                    self.rect.x -= SPEED
                if self.left:
                    self.rect.x += SPEED
                if self.jump:
                    self.rect.y += JUMP
                if not self.ground:
                    self.ground = True
                    self.rect.bottom = tile.rect.top


class Watergirl(pygame.sprite.Sprite):
    image = load_image("watergirl_stay2.png")

    def __init__(self, x, y):
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.right = False
        self.left = False
        self.jump = False
        self.ground = False
        self.deltax = 0
        self.deltay = 0


    def update(self, tiles):
        if self.right:
            self.deltax += SPEED
        if self.left:
            self.deltax -= SPEED
        if self.jump:
            if self.ground:
                self.deltay -= JUMP
        if not self.ground:
            self.deltay += GRAVITY
        self.rect.x += self.deltax
        self.rect.y += self.deltay
        self.collide(tiles)


    def collide(self, tiles):
        for tile in tiles:
            if pygame.sprite.collide_rect(self, tile):
                if self.right and self.rect.right >= tile.rect.left:
                    self.deltax -= SPEED
                if self.left and self.rect.left <= tile.rect.left:
                    self.deltax += SPEED
                if self.jump:
                    self.deltay += JUMP
                if not self.ground:
                    self.ground = True
                    self.rect.bottom = tile.rect.top


class Tiles(pygame.sprite.Sprite):
    image = load_image('wall.png')

    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    def update(self, *args):
        pass