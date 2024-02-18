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
    image1 = pygame.transform.scale(image, CHARACTER_SIZE)
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
            self.deltax = SPEED
        if self.left:
            self.deltax = -SPEED
        if not (self.left or self.right):
            self.deltax = 0
        if self.jump:
            if self.ground:
                self.deltay -= JUMP
        if not self.ground:
            self.deltay += GRAVITY
        self.ground = False
        self.rect.y += self.deltay
        self.collide(0, self.deltay, tiles)
        self.rect.x += self.deltax
        self.collide(self.deltax,0, tiles)

    def collide(self, deltax, deltay, tiles):
        for tile in tiles:
            if pygame.sprite.collide_rect(self, tile):
                if deltax > 0:
                    self.rect.right = tile.rect.left
                if deltax < 0:
                    self.rect.left = tile.rect.right
                if deltay < 0:
                    self.rect.top = tile.rect.bottom
                    self.deltay = 0
                if deltay > 0:
                    self.ground = True
                    self.rect.bottom = tile.rect.top
                    self.deltay = 0

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
            self.deltax = SPEED
        if self.left:
            self.deltax = -SPEED
        if not (self.left or self.right):
            self.deltax = 0
        if self.jump:
            if self.ground:
                self.deltay -= JUMP
        if not self.ground:
            self.deltay += GRAVITY
        self.ground = False
        self.rect.y += self.deltay
        self.collide(0, self.deltay, tiles)
        self.rect.x += self.deltax
        self.collide(self.deltax, 0, tiles)

    def collide(self, deltax, deltay, tiles):
        for tile in tiles:
            if pygame.sprite.collide_rect(self, tile):
                if deltax > 0:
                    self.rect.right = tile.rect.left
                if deltax < 0:
                    self.rect.left = tile.rect.right
                if deltay < 0:
                    self.rect.top = tile.rect.bottom
                    self.deltay = 0
                if deltay > 0:
                    self.ground = True
                    self.rect.bottom = tile.rect.top
                    self.deltay = 0


class Tiles(pygame.sprite.Sprite):
    image = load_image('wall.png')

    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    def update(self, *args):
        pass