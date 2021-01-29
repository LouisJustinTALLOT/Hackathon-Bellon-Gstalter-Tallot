import pygame as pg, sys
from random import randint
import src.get_levels as gl
import numpy as np

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
    global images
    n, m = len(matrice), len(matrice[0])
    for i in range(n):
        for j in range(m):
            screen.blit(images[matrice[j][i]], (16*i, 16*j))
            
list_levels = gl.load_all_levels()
mat = list_levels[0].matrice_niveau
n, m = len(mat), len(mat[0])

images = [pg.image.load("images/sol.png"), pg.image.load("images/heros.png"), pg.image.load("images/mur.png")] #images à afficher
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