import pygame
from characters import Fireboy, Watergirl
from const import *
from level import Fireboy_and_Watergirl
from records_list import create_list


def start_window(achievements=None):
    if achievements is None:
        achievements = {}
    greet = pygame.image.load('data/greeting_screen.png')
    screen.blit(greet, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 248 <= event.pos[0] <= 360 and 315 <= event.pos[1] < 370:
                    levels_window(achievements)
                if 210 <= event.pos[0] <= 410 and 385 <= event.pos[1] < 410:
                    records(True, achievements)


def levels_window(achievements):
    im = pygame.image.load('data/select_level.png')
    im = pygame.transform.scale(im, WINDOW_SIZE)
    screen.blit(im, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 190 <= event.pos[0] <= 425:
                    if 200 <= event.pos[1] < 240:
                        change_level(1, achievements)
                    elif 340 <= event.pos[1] < 380:
                        change_level(2, achievements)
                    elif 480 <= event.pos[1] <= 520:
                        change_level(3, achievements)


def change_level(level, achievements):
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
    game_on(level, achievements, all_sprites, boy, girl, tiles, fire_crystal, water_crystal, water_ponds, fire_ponds, boy_door, girl_door)


def victory(level, achievements, boy, girl, ticks):
    pygame.mouse.set_visible(1)
    records(False, achievements, level, boy, girl, ticks)
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
                    start_window(achievements)
                elif 200 <= event.pos[0] < 445 and 410 <= event.pos[1] < 445:
                    change_level(level, achievements)


def records(show, achievements, *args):
    if args:
        level, boy, girl, ticks = args
        if level not in achievements.keys():
            achievements[level] = [ticks, boy.fire_count + girl.water_count]
        elif ticks < achievements[level][0] and boy.fire_count + girl.water_count >= achievements[level][1]:
            achievements[level] = [ticks, boy.fire_count + girl.water_count]
    if show:
        create_list(achievements)
        im = pygame.image.load("data/new_rec.png")
        im = pygame.transform.scale(im, WINDOW_SIZE)
        screen.blit(im, (0, 0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 205 <= event.pos[0] < 385 and 510 <= event.pos[1] < 595:
                        levels_window(achievements)



def game_on(level, achievements, all_sprites, boy, girl, tiles, fire_crystal, water_crystal, water_ponds, fire_ponds, boy_door, girl_door):
    pygame.mouse.set_visible(0)
    clock = pygame.time.Clock()
    while True:
        ticks = pygame.time.get_ticks()
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
            fail(level, achievements)
        if boy.indoor and girl.indoor:
            pygame.time.delay(1000)
            victory(level, achievements, boy, girl, ticks)
        pygame.display.flip()
        pygame.display.flip()
        clock.tick(FPS)


def fail(level, achievements):
    pygame.mouse.set_visible(1)
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
                    start_window(achievements)
                elif 200 <= event.pos[0] < 445 and 410 <= event.pos[1] < 445:
                    change_level(level, achievements)

def close():
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen_back = pygame.Surface(WINDOW_SIZE)
    pygame.display.set_caption('Огонь и вода')
    start_window()

