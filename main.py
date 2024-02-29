import pygame
from characters import Fireboy, Watergirl
from const import *
from level import Fireboy_and_Watergirl

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen_back = pygame.Surface(WINDOW_SIZE)
    pygame.display.set_caption('Огонь и вода')
    im = pygame.image.load('data/greeting_screen.png')
    screen.blit(im, (0, 0))
    clock = pygame.time.Clock()
    select_level = False
    game_on = False
    change_level = 0
    end_screen = False
    running = True
    while running:
        if select_level:
            im = pygame.image.load('data/select_level.png')
            screen.blit(im, (0, 0))
        if game_on:
            screen.fill((0, 0, 0))
            screen.blit(screen_back, (0, 0))
            all_sprites.update(tiles, fire_crystal, water_crystal, fire_count, water_count, boy_door, girl_door)
            all_sprites.draw(screen)
        elif change_level:
            all_sprites = pygame.sprite.Group()
            tiles = pygame.sprite.Group()
            fire_crystal = pygame.sprite.Group()
            water_crystal = pygame.sprite.Group()
            boy_door = pygame.sprite.Group()
            girl_door = pygame.sprite.Group()
            fire_count = 0
            water_count = 0
            fb_wg = Fireboy_and_Watergirl(change_level)
            boy_coor, girl_coor = fb_wg.render(screen_back, tiles, fire_crystal, water_crystal, boy_door, girl_door)
            tiles.draw(screen_back)
            game_on = True
            change_level = 0
            select_level = False
            girl = Watergirl(*girl_coor)
            boy = Fireboy(*boy_coor)
            all_sprites.add(girl)
            all_sprites.add(boy)
            all_sprites.add(water_crystal)
            all_sprites.add(fire_crystal)
            all_sprites.add(boy_door)
            all_sprites.add(girl_door)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_on:
                if boy.boy_finish() and girl.girl_finish():
                    im = pygame.image.load('data/victory.png')
                    im = pygame.transform.scale(im, WINDOW_SIZE)
                    screen.blit(im, (0, 0))
                    game_on = False
                    end_screen = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if select_level and not change_level:
                    if event.pos[1] < 200:
                        change_level = 1
                    elif 200 <= event.pos[1] < 400:
                        change_level = 2
                    else:
                        change_level = 3
                if not game_on and not change_level:
                    if 248 <= event.pos[0] <= 360:
                        if 315 <= event.pos[1] < 370:
                            select_level = True
                if end_screen:
                    if 270 <= event.pos[1] < 370 and (230 <= event.pos[0] < 420 or 260 <= event.pos[0] < 395):
                        select_level = True
                    elif 200 <= event.pos[0] < 445 and 410 <= event.pos[1] < 445:
                        change_level = fb_wg.level()
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
