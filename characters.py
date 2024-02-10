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

    def key_reaction(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_UP:
                    pass

    def move(self):
        if self.right:
            self.coord = (self.coord[0] + SPEED, self.coord[1])
        if self.left:
            self.coord = (self.coord[0] - SPEED, self.coord[1])


class Watergirl(pygame.sprite.Sprite):
    image = load_image("watergirl_stay1.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Watergirl.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 0
        self.right = False
        self.left = False
        self.jump = False
        self.coord = (0, 0)

    def key_reaction(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.right = True
                if event.key == pygame.K_a:
                    self.left = True
                if event.key == pygame.K_w:
                    pass

    def move(self):
        if self.right:
            self.coord = (self.coord[0] + SPEED, self.coord[1])
        if self.left:
            self.coord = (self.coord[0] - SPEED, self.coord[1])
