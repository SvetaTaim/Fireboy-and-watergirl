import pygame
import os
import sys


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Fireboy(pygame.sprite.Sprite):
    image = load_image("fireboy.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Fireboy.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.right = False
        self.left = False
        self.jump = False
        self.coord = (0, 0)

    def move(self):
        if self.right:
            self.coord = (self.coord[0] + SPEED, self.coord[1])
        if self.left:
            self.coord = (self.coord[0] - SPEED, self.coord[1])



class Watergirl(pygame.sprite.Sprite):
    image = load_image("watergirl.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Fireboy.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.right = False
        self.left = False
        self.jump = False
        self.coord = (0, 0)

    def move(self):
        if self.right:
            self.coord = (self.coord[0] + SPEED, self.coord[1])
        if self.left:
            self.coord = (self.coord[0] - SPEED, self.coord[1])