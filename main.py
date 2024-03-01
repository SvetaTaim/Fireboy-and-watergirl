import pygame
from characters import Fireboy, Watergirl
from const import *
from level import Fireboy_and_Watergirl


def start_window():
    greet = pygame.image.load('data/greeting_screen.png')
    screen.blit(greet, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 248 <= event.pos[0] <= 360:
                    if 315 <= event.pos[1] < 370:
                        levels_window()


def levels_window():
    im = pygame.image.load('data/select_level.png')
    im = pygame.transform.scale(im, WINDOW_SIZE)
    screen.blit(im, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 128 <= event.pos[0] <= 480:
                    if 224 <= event.pos[1] < 320:
                        change_level(1)
                    elif 320 <= event.pos[1] < 416:
                        change_level(2)
                    elif 416 <= event.pos[1] <= 512:
                        change_level(3)


def change_level(level):
    all_sprites = pygame.sprite.Group()
    tiles = pygame.sprite.Group()
    fire_crystal = pygame.sprite.Group()
    water_crystal = pygame.sprite.Group()
    boy_door = pygame.sprite.Group()
    girl_door = pygame.sprite.Group()
    water_ponds = pygame.sprite.Group()
    fire_ponds = pygame.sprite.Group()
    fb_wg = Fireboy_and_Watergirl(level)
    coor = fb_wg.render(screen_back, tiles, fire_crystal, water_crystal, boy_door, girl_door, water_ponds, fire_ponds)
    tiles.draw(screen_back)
    boy = Fireboy(*coor[0])
    girl = Watergirl(*coor[1])
    all_sprites.add(water_crystal)
    all_sprites.add(fire_crystal)
    all_sprites.add(boy_door)
    all_sprites.add(girl_door)
    all_sprites.add(water_ponds)
    all_sprites.add(fire_ponds)
    all_sprites.add(girl)
    all_sprites.add(boy)
    game_on(level, all_sprites, boy, girl, tiles, fire_crystal, water_crystal, water_ponds, fire_ponds, boy_door, girl_door)


def victory(level, boy, girl):
    im = pygame.image.load('data/victory.png')
    im = pygame.transform.scale(im, WINDOW_SIZE)
    screen.blit(im, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 270 <= event.pos[1] < 370 and (230 <= event.pos[0] < 420 or 260 <= event.pos[0] < 395):
                    levels_window()
                elif 200 <= event.pos[0] < 445 and 410 <= event.pos[1] < 445:
                    change_level(level)


def records(level, boy, girl, time, show=False):
    records[level] = time, boy.fire_count + girl.water_count
    if show:
        im = pygame.image.load('data/records.png')
        im = pygame.transform.scale(im, WINDOW_SIZE)
        screen.blit(im, (0, 0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 270 <= event.pos[1] < 370 and (230 <= event.pos[0] < 420 or 260 <= event.pos[0] < 395):
                        levels_window()


def game_on(level, all_sprites, boy, girl, tiles, fire_crystal, water_crystal, water_ponds, fire_ponds, boy_door, girl_door):
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
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
        screen.fill((0, 0, 0))
        screen.blit(screen_back, (0, 0))
        all_sprites.update(tiles, fire_crystal, water_crystal, water_ponds, fire_ponds, boy_door, girl_door)
        all_sprites.draw(screen)
        if not boy.live or not girl.live:
            pygame.time.delay(1000)
            fail(level)
        if boy.indoor and girl.indoor:
            pygame.time.delay(1000)
            victory(level, boy, girl)
        pygame.display.flip()
        clock.tick(FPS)


def fail(level):
    im = pygame.image.load('data/game_over.png')
    im = pygame.transform.scale(im, WINDOW_SIZE)
    screen.blit(im, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 270 <= event.pos[1] < 370 and (230 <= event.pos[0] < 420 or 260 <= event.pos[0] < 395):
                    levels_window()
                elif 200 <= event.pos[0] < 445 and 410 <= event.pos[1] < 445:
                    change_level(level)

def close():
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen_back = pygame.Surface(WINDOW_SIZE)
    pygame.display.set_caption('Огонь и вода')
    start_window()

