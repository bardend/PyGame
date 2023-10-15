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
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 255, 255)

 
class Boar():
    def __init__(self, settings):
        self.boar = None
        self.settings = settings

    def fill_boar(self):
        numeros_disponibles = list(range(9))
        vec_num = random.sample(numeros_disponibles, self.settings.row * self.settings.col)
        self.boar = [vec_num[i:i+self.settings.row] for i in range(0,9,self.settings.col)]

    def get_boar(self):
        return self.boar

class Boar_gen(Boar): #Generate a boar after moving one piece
    def __init__(self, settings, pre_boar):
        super().__init__(settings)
        self.pre_boar = pre_boar

    def move(self):
        positions = next(((i, j) for i,row in enumerate(self.pre_boar) for j,val in enumerate(row) if val == 0), None)

        vec_new_boar = []

        for i in range(0,4):
            #pre_boar = self.pre_boar.copy()
            pre_boar = copy.deepcopy(self.pre_boar)
            new_pos = (positions[0] + self.settings.movex[i], positions[1] + self.settings.movey[i])
            if(new_pos[0]<self.settings.lower_bound or new_pos[0]>=self.settings.upper_bound or new_pos[1]<self.settings.lower_bound or new_pos[1]>=self.settings.upper_bound):
                continue
            print(new_pos)
            print(positions)
            cur_boar = swap(pre_boar, positions[0], positions[1], new_pos[0], new_pos[1])
            vec_new_boar.append(cur_boar)
        return vec_new_boar
