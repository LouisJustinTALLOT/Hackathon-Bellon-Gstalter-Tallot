import pygame as pg
import numpy as np
from random import randint

import sys
sys.path.insert(1, './src')

import get_levels as gl

def init(n, m):
    screen = pg.display.set_mode((16*n, 16*m))
    return screen

def affichage(screen, matrice):
    global images
    n, m = len(matrice), len(matrice[0])
    for i in range(n):
        for j in range(m):
            screen.blit(images[matrice[i][j]], (16*j, 16*i))


images = [pg.image.load("images/sol.png"), pg.image.load("images/heros.png"), pg.image.load("images/mur.png")] #images à afficher




# section de test 

if __name__ == "__main__": 
    list_levels = gl.load_all_levels()
    mat = list_levels[0].matrice_niveau

    n, m = len(mat), len(mat[0])

    screen = init(m, n)
    affichage(screen, mat)

    clock = pg.time.Clock()
    running = True
    while running:
        clock.tick(1)
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        running = False       
        pg.display.update()
    pg.quit()