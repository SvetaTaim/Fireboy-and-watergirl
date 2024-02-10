import pygame
import pytmx
from characters import Fireboy, Watergirl
from const import *
from level import Fireboy_and_Watergirl

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    fb_wg = Fireboy_and_Watergirl("main_window.tmx", [10, 46], 20)
    change_level = 0
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not change_level:
                    if 128 <= event.pos[0] <= 480:
                        if 224 <= event.pos[1] < 320:
                            change_level = 1
                        elif 320 <= event.pos[1] < 416:
                            change_level = 2
                        elif 416 <= event.pos[1] <= 512:
                            change_level = 3
            if change_level:
                fb_wg = Fireboy_and_Watergirl(f"map{change_level}.tmx", [10, 46], 20)
                pygame.display.flip()
        fb_wg.render(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
