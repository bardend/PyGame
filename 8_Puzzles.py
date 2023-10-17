import pygame
import sys
from boar import Settings,Boar
from Queue import *
from Sketcher import Sketcher
from Settings import Settings
import Game_functions as gf

def run_game():
    sett = set()
    on = 0
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("8_Puzzles")
    my_boar = Boar(settings.base, (10,700), settings, 0)
    sketcher = Sketcher(screen, settings)

    q = Queue()
    q.push(my_boar)

    while True:
        gf.check_events(on, q, sketcher, sett)
        gf.update_screen(settings, screen, sketcher)
run_game()
