import pygame
from characters import Fireboy, Watergirl
from const import *
from level import Fireboy_and_Watergirl

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen_back = pygame.Surface(WINDOW_SIZE)
    pygame.display.set_caption('Огонь и вода')
    greet = pygame.image.load('data/greeting_screen.png')
    screen.blit(greet, (0, 0))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    tiles = pygame.sprite.Group()
    fire_crystal = pygame.sprite.Group()
    water_crystal = pygame.sprite.Group()
    fire_count = 0
    water_count = 0
    new_game = False
    game_on = False
    change_level = 0
    running = True
    while running:
        if new_game:
            screen.fill((255, 255, 255))
        if game_on:
            screen.fill((0, 0, 0))
            screen.blit(screen_back, (0, 0))
            all_sprites.update(tiles, fire_crystal, water_crystal, fire_count, water_count)
            all_sprites.draw(screen)
        elif change_level:
            fb_wg = Fireboy_and_Watergirl(f"map{change_level}.txt", [10, 46], 20)
            coor = fb_wg.render(screen_back, tiles, fire_crystal, water_crystal)
            tiles.draw(screen_back)
            game_on = True
            change_level = False
            new_game = False
            boy = Fireboy(*coor[0])
            girl = Watergirl(*coor[1])
            all_sprites.add(girl)
            all_sprites.add(boy)
            all_sprites.add(water_crystal)
            all_sprites.add(fire_crystal)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game and not change_level:
                    if 128 <= event.pos[0] <= 480:
                        if 224 <= event.pos[1] < 320:
                            change_level = 1
                        elif 320 <= event.pos[1] < 416:
                            change_level = 2
                        elif 416 <= event.pos[1] <= 512:
                            change_level = 3
                if not game_on and not change_level:
                    if 248 <= event.pos[0] <= 360:
                        if 315 <= event.pos[1] < 370:
                            new_game = True
            if event.type == pygame.KEYDOWN:
                if game_on:
                    if event.key == pygame.K_RIGHT:
                        boy.right = True
                    if event.key == pygame.K_LEFT:
                        boy.left = True
                    if event.key == pygame.K_UP:
                        boy.jump = True
                    if event.key == pygame.K_d:
                        girl.right = True
                    if event.key == pygame.K_a:
                        girl.left = True
                    if event.key == pygame.K_w:
                        girl.jump = True
            if event.type == pygame.KEYUP:
                if game_on:
                    if event.key == pygame.K_RIGHT:
                        boy.right = False
                    if event.key == pygame.K_LEFT:
                        boy.left = False
                    if event.key == pygame.K_UP:
                        boy.jump = False
                    if event.key == pygame.K_d:
                        girl.right = False
                    if event.key == pygame.K_a:
                        girl.left = False
                    if event.key == pygame.K_w:
                        girl.jump = False
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
