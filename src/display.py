import pygame as pg
import numpy as np
from random import randint

import sys
sys.path.insert(1, './src')

import get_levels as gl
import src.heros as heros


pg.init()

sysfont = pg.font.get_default_font()
myfont = pg.font.SysFont(None, 20)
print("font importées")

def init(n, m):
    screen = pg.display.set_mode((16*n, 16*(m+4)))
    return screen

def affichage(screen, matrice, images, perso:heros.Heros):
    n, m = len(matrice), len(matrice[0])
    # n hauteur, m longueur
    for i in range(n):
        for j in range(m):
            screen.blit(images[matrice[i][j]], (16*j, 16*i))

    black_rect = pg.Rect(0, 16*n, 16*m, 16*4)
    pg.draw.rect(screen, (0, 0, 0), black_rect)

    textsurface = myfont.render('LIFE : '+str(perso.vie), False, (255, 255, 255))
    screen.blit(textsurface,(3*m,16*(n+2)))

    textsurface2 = myfont.render('FAIM : '+str(perso.faim), False, (255, 255, 255))
    screen.blit(textsurface2,(5*m,16*(n+2)))

    textsurface3 = myfont.render('SCORE : '+str(perso.score), False, (255, 255, 255))
    screen.blit(textsurface3,(7*m,16*(n+2)))

    textsurface4 = myfont.render('ETAT : '+str(perso.etat), False, (255, 255, 255))
    screen.blit(textsurface4,(9*m,16*(n+2)))

    if perso.epee:
        screen.blit(images[8], (11*m, 16*(n+2)))
    else:
        screen.blit(images[21], (11*m, 16*(n+2)))

    if perso.argent:
        screen.blit(images[9], (13*m+16, 16*(n+2)))
        textsurface5 = myfont.render(str(perso.argent), False, (255, 255, 255))
        screen.blit(textsurface5,(13*m,16*(n+2)))
        # print(perso.argent)
    else:
        screen.blit(images[21], (13*m+16, 16*(n+2)))
    # print(perso.faim)
    # print(perso.etat)

def gagne_ou_perdu(screen, messages, i, perso:heros.Heros):
    screen = pg.display.set_mode((400, 350))
    black_rect = pg.Rect(0, 0, 400, 300)
    pg.draw.rect(screen, (0, 0, 0), black_rect)
    screen.blit(messages[i], (0, 0))
    textsurface = myfont.render('SCORE : '+str(perso.score), False, (255, 255, 255))
    screen.blit(textsurface,(150,320))

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