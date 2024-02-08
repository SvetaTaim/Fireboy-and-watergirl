import pygame
import pytmx
from level import Fireboy_and_Watergirl
from characters import Fireboy, Watergirl
from const import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    fb_wg = Fireboy_and_Watergirl("map1.tmx", [10, 46], 20)
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    boy = Fireboy()
    girl = Watergirl()
    all_sprites.add(boy)
    all_sprites.add(girl)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        fb_wg.render(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
