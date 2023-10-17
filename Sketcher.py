import pygame
import sys
from boar import Settings,Boar
from Queue import *
from Settings import Settings

class Sketcher():
    def __init__(self, screen, settings):
        self.screen = screen
        self.vec_boar = []
        self.settings = settings

    def add_boar(self, boar):
        self.vec_boar.append(boar)

    def draw(self):
        font = pygame.font.Font(None, 30)
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
