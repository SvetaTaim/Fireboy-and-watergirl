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
    image_stay1 = load_image("fireboy_stay1.png")
    image_stay2 = load_image('fireboy_stay2.png')
    image_right1 = load_image('fireboy_right1.png')
    image_right2 = load_image('fireboy_right2.png')
    image_left1 = pygame.transform.flip(image_right1, True, False)
    image_left1.set_colorkey((255, 255, 255))
    image_left2 = pygame.transform.flip(image_right2, True, False)
    image_left2.set_colorkey((255, 255, 255))

    def __init__(self, x, y):
        super().__init__()
        self.image = Fireboy.image_stay1
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
            if self.image != Fireboy.image_right1:
                self.image = Fireboy.image_right1
            else:
                self.image = Fireboy.image_right2
        if self.left:
            self.deltax = -SPEED
            if self.image != Fireboy.image_left1:
                self.image = Fireboy.image_left1
            else:
                self.image = Fireboy.image_left2
        if not (self.left or self.right):
            self.deltax = 0
            if self.image != Fireboy.image_stay1:
                self.image = Fireboy.image_stay1
            else:
                self.image = Fireboy.image_stay2
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
            if pygame.sprite.collide_mask(self, tile):
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
    image_stay1 = load_image("watergirl_stay1.png")
    image_stay2 = load_image('watergirl_stay2.png')
    image_right1 = load_image('watergirl_right1.png')
    image_right2 = load_image('watergirl_right2.png')
    image_left1 = pygame.transform.flip(image_right1, True, False)
    image_left1.set_colorkey((255, 255, 255))
    image_left2 = pygame.transform.flip(image_right2, True, False)
    image_left2.set_colorkey((255, 255, 255))

    def __init__(self, x, y):
        super().__init__()
        self.image = Watergirl.image_stay1
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
            if self.image != Watergirl.image_right1:
                self.image = Watergirl.image_right1
            else:
                self.image = Watergirl.image_right2
        if self.left:
            self.deltax = -SPEED
            if self.image != Watergirl.image_left1:
                self.image = Watergirl.image_left1
            else:
                self.image = Watergirl.image_left2
        if not (self.left or self.right):
            self.deltax = 0
            if self.image != Watergirl.image_stay1:
                self.image = Watergirl.image_stay1
            else:
                self.image = Watergirl.image_stay2
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
            if pygame.sprite.collide_mask(self, tile):
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