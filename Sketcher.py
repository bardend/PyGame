import pygame
import sys

from boar import Settings,Boar

SCREEN_SIZE = 800
GRID_SIZE = 3
CELL_SIZE = 40
GRID_X = 10  # Posición X en la que comienza el crucigrama
GRID_Y = 300  # Posición Y en la que comienza el crucigrama
WHITE = (255, 255, 255)

class Sketcher():
    def __init__(self, screen, boar, posx, posy, settings):
        self.screen = screen
        self.boar = boar
        self.posx = posx
        self.posy = posy
        self.settings = settings

    def draw(self):

        font = pygame.font.Font(None, 50)
        for i in range(self.settings.row):
            for j in range(self.settings.col):
                #print(i,j)
                number = self.boar.get_boar()[i][j]
                text = font.render(str(number), True, (0,0,0))
                self.screen.blit(text, (self.posx + i * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2, self.posy + j * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2))

#self.bg_color = (230, 230, 230)

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("8_Puzzles")
    my_boar = Boar(settings)
    my_boar.fill_boar()
    sketcher = Sketcher(screen, my_boar, GRID_X, GRID_Y, settings)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(settings.bg_color)
        sketcher.draw()
        pygame.display.flip()
run_game()
