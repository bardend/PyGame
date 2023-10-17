import random
import pygame
import copy
from Settings import Settings

def swap(boar, i, j, ii, jj):
    tmp = boar.copy()
    x = boar[i][j]
    y = boar[ii][jj]
    tmp[i][j] = y
    tmp[ii][jj] = x
    return tmp


class Boar():
    def __init__(self, boar, pos, settings, deep):
        self.boar = boar
        self.pos = pos
        self.settings = settings
        self.deep = deep

    def gen_boar(self):
        movex = 250
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
        coor = (self.pos[0]+movex, self.pos[1] - (len(vec_new_boar)*20)*(3-self.deep)*(3-self.deep))
        ret = []
        for ind,e in enumerate(vec_new_boar):
            new_coor = (coor[0], coor[1] + 20*ind*(4-self.deep)*(4-self.deep))
            ret.append(Boar(e, new_coor, self.settings, self.deep+1))
            print(new_coor)
                       
        return ret

