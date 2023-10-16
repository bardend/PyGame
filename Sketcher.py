import pygame
import sys
from boar import Settings,Boar
#from Queue import *
class Sketcher():
    def __init__(self, screen, settings):
        self.screen = screen
        self.vec_boar = []
        self.settings = settings

    def add_boar(self, boar):
        self.vec_boar.append(boar)

    def draw(self):
        font = pygame.font.Font(None, 50)
        for ele in self.vec_boar:
            for i in range(self.settings.row):
                for j in range(self.settings.col):
                    number = ele.boar[i][j]
                    text = font.render(str(number), True, (0,0,0))
                    self.screen.blit(text, (ele.pos[0] + i * self.settings.cell_size + self.settings.cell_size // 2 - text.get_width() // 2, ele.pos[1] + j * self.settings.cell_size + self.settings.cell_size // 2 - text.get_height() // 2))

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("8_Puzzles")
    my_boar = Boar(settings.base, (10,300), settings)

    sketcher = Sketcher(screen, settings)
    sketcher.add_boar(my_boar)

    xd = my_boar.gen_boar()
    print(len(xd))

    
    for e in xd:
        sketcher.add_boar(e)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                cnt+=1

        screen.fill(settings.bg_color)
        sketcher.draw()
        pygame.display.flip()

run_game()
