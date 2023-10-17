import pygame
import sys
from boar import Settings,Boar
from Queue import *
sett = set()
class Sketcher():
    def __init__(self, screen, settings):
        self.screen = screen
        self.vec_boar = []
        self.settings = settings

    def add_boar(self, boar):
        self.vec_boar.append(boar)

   def draw(self):
        font = pygame.font.Font(None, 20)
        for ele in self.vec_boar:
            for i in range(self.settings.row):
                for j in range(self.settings.col):
                    pygame.draw.rect(self.screen, (0, 0, 0), (ele.pos[0] + j * self.settings.cell_size, ele.pos[1] + i * self.settings.cell_size, self.settings.cell_size, self.settings.cell_size), 1)
                    number = ele.boar[i][j]
                    if number >0 :
                        text = font.render(str(number), True, (0,0,0))
                        self.screen.blit(text, (ele.pos[0] + i * self.settings.cell_size + self.settings.cell_size // 2 - text.get_width() // 2, ele.pos[1] + j * self.settings.cell_size + self.settings.cell_size // 2 - text.get_height() // 2))
                    else :
                        pygame.draw.rect(self.screen, (255, 0, 0), (ele.pos[0] + i * self.settings.cell_size, ele.pos[1] + j * self.settings.cell_size, self.settings.cell_size, self.settings.cell_size), 0)


def run_game():
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                on = 1
        
        while q.isEmpty() == False:
            v = q.front()
            if on == 0 : #Apagado
                break
            on = 0
            q.pop()
            sketcher.add_boar(v)
            sett.add(v)
            xd = v.gen_boar()
            for e in xd:
                if e not in sett:
                    q.push(e)

        screen.fill(settings.bg_color)
        sketcher.draw()
        pygame.display.flip()
run_game()
