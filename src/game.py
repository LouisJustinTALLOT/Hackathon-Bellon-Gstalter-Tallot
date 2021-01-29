import pygame as pg
import numpy as np

# fichiers maisons
import src.get_levels as gl
import src.display as display
import src.heros as heros

def init_level(list_levels, i):
    level = list_levels[i]
    mat = level.matrice_niveau
    bool_matrice = np.ones((len(mat), len(mat[0])))
    x0, y0 = level.depart_heros_x, level.depart_heros_y
    return [mat, x0, y0]

def play_game(screen, perso, mat, images):
    running = True
    has_changed = True
    while running:
        # clock.tick(1)
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    has_changed = True

                    if event.key == pg.K_q:
                        running = False
                    if event.key == pg.K_UP:
                        perso.deplacement((0,-1), mat)
                    if event.key == pg.K_DOWN:
                        perso.deplacement((0,1), mat)
                    if event.key == pg.K_RIGHT:
                        perso.deplacement((1,0), mat)
                    if event.key == pg.K_LEFT:
                        perso.deplacement((-1,0), mat)
        if has_changed:
            display.affichage(screen, mat, images,perso)
            has_changed = False
            pg.display.update()
        if perso.escalier:
            perso.escalier = False
            return 1 #on va passer au niveau suivant
        if perso.vie == 0:
            return 0 #game_over
        if perso.etat <= 0:
            perso.vie -= 1
            perso.etat = 100
    return 0