import pygame
import os
import sys


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
        self.coord = (0, 0)

    def move(self):
        if self.right:
            self.coord = (self.coord[0] + SPEED, self.coord[1])
        if self.left:
            self.coord = (self.coord[0] - SPEED, self.coord[1])
        if self.jump:
            if self.ground:
                self.coord = (self.coord[0], self.coord[1] - JUMP)
        if not self.ground:
            self.coord = (self.coord[0], self.coord[1] + GRAVITY)


class Watergirl(pygame.sprite.Sprite):
    image = load_image("watergirl_stay1.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Watergirl.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.right = False
        self.left = False
        self.jump = False
        self.ground = False
        self.coord = (0, 0)

    def move(self):
        if self.right:
            self.coord = (self.coord[0] + SPEED, self.coord[1])
        if self.left:
            self.coord = (self.coord[0] - SPEED, self.coord[1])
        if self.jump:
            if self.ground:
                self.coord = (self.coord[0], self.coord[1] - JUMP)
        if not self.ground:
            self.coord = (self.coord[0], self.coord[1] + GRAVITY)

    def draw(self, screen):
        screen.blit(self.image, self.coord)


