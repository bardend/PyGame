import random
import pygame
import copy

def swap(boar, i, j, ii, jj):
    tmp = boar.copy()
    x = boar[i][j]
    y = boar[ii][jj]
    tmp[i][j] = y
    tmp[ii][jj] = x
    return tmp

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
        self.cell_size = 40
        numeros_disponibles = list(range(9))
        vec_num = random.sample(numeros_disponibles, self.row * self.col)
        self.base = [vec_num[i:i+self.row] for i in range(0,9,self.col)]

class Boar():
    def __init__(self, boar, pos, settings):
        self.boar = boar
        self.pos = pos
        self.settings = settings

    def gen_boar(self):
        movex = 160
        positions = next(((i, j) for i,row in enumerate(self.boar) for j,val in enumerate(row) if val == 0), None)
        vec_new_boar = []
        for i in range(0,4):
            pre_boar = copy.deepcopy(self.boar)
            new_pos = (positions[0] + self.settings.movex[i], positions[1] + self.settings.movey[i])
            if(new_pos[0]<self.settings.lower_bound or new_pos[0]>=self.settings.upper_bound or new_pos[1]<self.settings.lower_bound or new_pos[1]>=self.settings.upper_bound):
                continue
            cur_boar = swap(pre_boar, positions[0], positions[1], new_pos[0], new_pos[1])
            vec_new_boar.append(cur_boar)
        ### How many boars are there and generate a the pos of the new boars 
        coor = (self.pos[0]+movex, self.pos[1] - (len(vec_new_boar)*140//2))
        ret = []
        for ind,e in enumerate(vec_new_boar):
            new_coor = (coor[0], coor[1] + 140*ind)
            ret.append(Boar(e, new_coor, self.settings))
                       
        return ret

settings = Settings()
my_boar = Boar(settings.base, (10,400), settings)
