import pygame
import pytmx
from characters import Fireboy, Watergirl
from const import *
from level import Fireboy_and_Watergirl

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Огонь и вода')
    screen.fill((255, 255,
                 255))  # Мила, придумай, как открывать начальную картинку. Я пока ее просто убрала, чтобы код заработал
    # Герои пока остаются на поле линией, потому что надо сделать нормально fb_wg. Я не совсем понимаю, что это, поэтому надеюсь на тебя
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    boy = Fireboy(100, 100)
    girl = Watergirl(200, 200)
    all_sprites.add(girl)
    all_sprites.add(boy)
    change_level = 0
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
            if event.type == pygame.KEYDOWN:
                if change_level:
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
                if change_level:
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
        # Убрала отрисовку уровня из цикла, исчезли остаточные изображения, подняла FPS, чтобы двигались плавнее
        if change_level:
            fb_wg = Fireboy_and_Watergirl(f"map{change_level}.txt", [10, 46], 20)
            fb_wg.render(screen)
        if change_level:
            all_sprites.update()
            all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
