import pygame
import sys
from boar import Settings,Boar
from Queue import *

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("8_Puzzles")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                off = 0
        
        screen.fill(settings.bg_color)
        print(off)
        pygame.display.flip()

run_game()
