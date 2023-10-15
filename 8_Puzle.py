import pygame
from boar import Settings,Boar


def run_game():
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("8_Puzzles")

    my_boar = Boar(settings)
    my_boar.fill_boar()
    print(my_boar.get_boar())

    """
    nxt = Boar_gen(my_settings, my_boar.get_boar())
    r = nxt.move()
    for e in r:
        print("===========")
        print(e)    
    """
run_game()
