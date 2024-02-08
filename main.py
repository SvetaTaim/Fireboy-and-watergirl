import pygame
import pytmx
from level import Fireboy_and_Watergirl
from const import WINDOW_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, FPS, MAPS_DIR, TILE_SIZE


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    fb_wg = Fireboy_and_Watergirl("map1.tmx", [10, 46], 20)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        fb_wg.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
