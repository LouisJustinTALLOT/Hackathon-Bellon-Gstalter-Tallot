import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
import sys
import random as rd
sys.path.insert(1, './src')

class Heros:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.vie = 3
        self.etat = 100
        self.faim = 100
        self.escalier = False
        self.epee = False
        self.clef = False
        self.score = 0
        self.argent = 0
        self.precedent = 0

    def deplacement(self, direction, matrice):
        x = self.x
        y = self.y
        x += direction[0]
        y += direction[1]

        if matrice[y][x] in [2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:     # mur
            self.etat -= 1

        elif matrice[y][x] == 0:   # sol
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                matrice[y][x] = 1
                self.x, self.y = x, y
                self.precedent = 0

        elif matrice[y][x] == 6:   # porte
            matrice[self.y][self.x] = self.precedent
            self.x, self.y = x, y
            matrice[self.y][self.x] = 1
            self.precedent = 6

        elif matrice[y][x] == 3:   # escalier
            self.escalier = True
            self.score += 100

        elif matrice[y][x] == 4:   # pomme
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.faim += 10
            self.score += 5

        elif matrice[y][x] == 5:   # monstre
            if self.epee:
                matrice[y][x] = 0
                self.score += 30
            else:
                self.etat -= 20

        elif matrice[y][x] == 7:   # potion
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.etat += 10
            self.score += 5
            self.precedent = 0

        elif matrice[y][x] == 8:   # épée
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.epee = True
            self.score += 50
            self.precedent = 0

        elif matrice[y][x] == 9:   # or
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.score += 20
            self.argent += rd.randint(1,20)
            self.precedent = 0

        elif matrice[y][x] == 20: #couloir
            if self.precedent in [20, 6]:
                matrice[y][x] = 1
                matrice[self.y][self.x] = self.precedent
                self.x, self.y = x, y
                self.precedent = 20
            else:
                self.etat -= 1

        elif matrice[y][x] == 22:   # clé
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.clef = True
            self.score += 10
            self.precedent = 0

        elif matrice[y][x] == 23: # eau
            self.etat -= self.ETAT_MAX
            matrice[self.y][self.x] = self.precedent
            self.x, self.y = self.x0, self.y0
            matrice[self.y][self.x] = 1

            self.precedent = 0