import pygame
import sys

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('play')
    image = pygame.image.load('images/得意.bmp')
    rect = image.get_rect()
    screen_rect = screen.get_rect()
    rect.centerx = screen_rect.centerx
    rect.centery = screen_rect.centery


    #开始游戏主循环
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((235, 225, 230))
        screen.blit(image, rect)


        pygame.display.flip()

run_game()
