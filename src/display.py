import pygame as pg
import numpy as np
from random import randint

import sys
sys.path.insert(1, './src')

import get_levels as gl

def init(n, m):
    screen = init_display(16*n, 16*m)
    return screen

def init_display(n, m):
    screen = pg.display.set_mode((n, m))
    screen.fill((89, 90, 92))
    return screen

def add_borders(screen, n, m):
    width = 5 # largeur du rectangle en pixels
    height = 5 # hauteur du rectangle en pixels
    color = (255, 255, 255) # couleur rouge
    for i in range(m):
        rect = pg.Rect(0, i, width, height)
        pg.draw.rect(screen, color, rect)
        rect = pg.Rect(n-5, i, width, height)
        pg.draw.rect(screen, color, rect)
    for i in range(n):
        rect = pg.Rect(i, 0, width, height)
        pg.draw.rect(screen, color, rect)
        rect = pg.Rect(i, m-5, width, height)
        pg.draw.rect(screen, color, rect)

def affichage(screen, matrice):
    images = [pg.image.load("images/sol.png"), pg.image.load("images/heros.png"), pg.image.load("images/mur.png")]
    n, m = len(matrice), len(matrice[0])
    for i in range(n):
        for j in range(m):
            screen.blit(images[matrice[i][j]], (16*i, 16*j))





# section de test 

if __name__ == "__main__": 
    list_levels = gl.load_all_levels()
    mat = list_levels[0].matrice_niveau

    mat = np.array(mat)
    mat = mat.T
    n, m = len(mat), len(mat[0])

    screen = init(n, m)
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