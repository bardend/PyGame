import random
class Settings():
    def __init__(self):
        self.row = 3
        self.col = 3
        self.movex = [1,0,-1,0]
        self.movey = [0,1,0,-1]
        self.lower_bound = 0
        self.upper_bound = 3
        self.screen_width = 1800
        self.screen_height = 1400
        self.bg_color = (0, 255, 255)
        self.cell_size = 30
        numeros_disponibles = list(range(9))
        vec_num = random.sample(numeros_disponibles, self.row * self.col)
        self.base = [vec_num[i:i+self.row] for i in range(0,9,self.col)]
