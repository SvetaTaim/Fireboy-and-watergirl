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

    def init(self, *group):
        super().init(*group)
        self.image = Fireboy.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, l=False, r=False, u=False):
        if l:
            self.rect.x -= STEP
        if r:
            self.rect.x += STEP
        if u:
            self.rect.y -= JUMP
        #здесь надо будет дописывать движение огня, пока что просто реакция на кнопочки


class Watergirl(pygame.sprite.Sprite):
    image = load_image("watergirl.png")

    def init(self, *group):
        super().init(*group)
        self.image = Fireboy.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, l=False, r=False, u=False):
        if l:
            self.rect.x -= STEP
        if r:
            self.rect.x += STEP
        if u:
            self.rect.y -= JUMP
        #здесь надо будет дописывать движение воды, пока что просто реакция на кнопочки