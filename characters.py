import pygame
import os
import sys
from const import *


def load_image(name, size, colorkey=(255, 255, 255)):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image1 = pygame.transform.scale(image, size)
    image1.set_colorkey(colorkey)
    return image1


class Fireboy(pygame.sprite.Sprite):
    image_stay1 = load_image("fireboy_stay1.png", CHARACTER_STAY_SIZE)
    image_stay2 = load_image('fireboy_stay2.png', CHARACTER_STAY_SIZE)
    image_right1 = load_image('fireboy_right1.png', CHARACTER_RUN_SIZE)
    image_right2 = load_image('fireboy_right2.png', CHARACTER_RUN_SIZE)
    image_left1 = pygame.transform.flip(image_right1, True, False)
    image_left1.set_colorkey((255, 255, 255))
    image_left2 = pygame.transform.flip(image_right2, True, False)
    image_left2.set_colorkey((255, 255, 255))

    def __init__(self, x=None, y=None):
        super().__init__()
        self.image = Fireboy.image_stay1
        self.rect = self.image.get_rect()
        if x and y:
            self.rect.x = x
            self.rect.y = y
        self.right = False
        self.left = False
        self.jump = False
        self.ground = False
        self.deltax = 0
        self.deltay = 0
        self.live = True
        self.finish = False
        self.indoor = False
        self.fire_count = 0

    def update(self, tiles, fire_crystal, water_crystal, water_ponds, fire_ponds, boy_door, girl_door):
        if self.right:
            self.deltax = SPEED
            if not self.jump:
                if self.image != Fireboy.image_right1:
                    self.image = Fireboy.image_right1
                else:
                    self.image = Fireboy.image_right2
            else:
                self.image = Fireboy.image_right2
        if self.left:
            self.deltax = -SPEED
            if not self.jump:
                if self.image != Fireboy.image_left1:
                    self.image = Fireboy.image_left1
                else:
                    self.image = Fireboy.image_left2
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
        self.collide(0, self.deltay, tiles, fire_crystal, water_ponds, boy_door)
        self.rect.x += self.deltax
        self.collide(self.deltax, 0, tiles, fire_crystal, water_ponds, boy_door)

    def collide(self, deltax, deltay, tiles, fire_crystal, water_ponds, boy_door):
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
        for crystal in fire_crystal:
            if pygame.sprite.collide_mask(self, crystal):
                self.fire_count += 1
                crystal.kill()
        for pond in water_ponds:
            if pygame.sprite.collide_mask(self, pond):
                self.live = False
        for door in boy_door:
            if pygame.sprite.collide_mask(self, door):
                self.indoor = True


class Watergirl(pygame.sprite.Sprite):
    image_stay1 = load_image("watergirl_stay1.png", CHARACTER_STAY_SIZE)
    image_stay2 = load_image('watergirl_stay2.png', CHARACTER_STAY_SIZE)
    image_right1 = load_image('watergirl_right1.png', CHARACTER_RUN_SIZE)
    image_right2 = load_image('watergirl_right2.png', CHARACTER_RUN_SIZE)
    image_left1 = pygame.transform.flip(image_right1, True, False)
    image_left1.set_colorkey((255, 255, 255))
    image_left2 = pygame.transform.flip(image_right2, True, False)
    image_left2.set_colorkey((255, 255, 255))

    def __init__(self, x=None, y=None):
        super().__init__()
        self.image = Watergirl.image_stay1
        self.rect = self.image.get_rect()
        if x and y:
            self.rect.x = x
            self.rect.y = y
        self.right = False
        self.left = False
        self.jump = False
        self.ground = False
        self.deltax = 0
        self.deltay = 0
        self.live = True
        self.finish = False
        self.indoor = False
        self.water_count = 0

    def update(self, tiles, fire_crystal, water_crystal, water_ponds, fire_ponds, boy_door, girl_door):
        if self.right:
            self.deltax = SPEED
            if not self.jump:
                if self.image != Watergirl.image_right1:
                    self.image = Watergirl.image_right1
                else:
                    self.image = Watergirl.image_right2
            else:
                self.image = Watergirl.image_right2
        if self.left:
            self.deltax = -SPEED
            if not self.jump:
                if self.image != Watergirl.image_left1:
                    self.image = Watergirl.image_left1
                else:
                    self.image = Watergirl.image_left2
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
        self.collide(0, self.deltay, tiles, water_crystal, fire_ponds, girl_door)
        self.rect.x += self.deltax
        self.collide(self.deltax, 0, tiles, water_crystal, fire_ponds, girl_door)

    def collide(self, deltax, deltay, tiles, water_crystal, fire_ponds, girl_door):
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
        for crystal in water_crystal:
            if pygame.sprite.collide_mask(self, crystal):
                self.water_count += 1
                crystal.kill()
        for pond in fire_ponds:
            if pygame.sprite.collide_mask(self, pond):
                self.live = False
        for door in girl_door:
            if pygame.sprite.collide_mask(self, door):
                self.indoor = True


class Tiles(pygame.sprite.Sprite):
    image = load_image('wall.png', (TILE_SIZE, TILE_SIZE))

    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.image = Tiles.image

    def update(self, *args):
        pass


class Crystal(pygame.sprite.Sprite):
    water_image = load_image('water_crystal.png', CRYSTAL_SIZE)
    fire_image = load_image('fire_crystal.png', CRYSTAL_SIZE)

    def __init__(self, x, y, color):
        super().__init__()
        self.rect = pygame.Rect((x, y), CRYSTAL_SIZE)
        if color == 'fire':
            self.image = Crystal.fire_image
        else:
            self.image = Crystal.water_image

class Door(pygame.sprite.Sprite):
    water_door = load_image('girl_door.png', DOOR_SIZE)
    boy_door = load_image('boy_door.png', DOOR_SIZE)

    def __init__(self, x, y, color):
        super().__init__()
        self.rect = pygame.Rect((x, y), DOOR_SIZE)
        if color == 'fire':
            self.image = Door.boy_door
        else:
            self.image = Door.water_door

class Pond(pygame.sprite.Sprite):
    water_pond = load_image('water_pond.png', POND_SIZE)
    fire_pond = load_image('fire_pond.png', POND_SIZE)

    def __init__(self, x, y, color):
        super().__init__()
        self.rect = pygame.Rect((x, y), POND_SIZE)
        if color == 'fire':
            self.image = Pond.fire_pond
        else:
            self.image = Pond.water_pond
