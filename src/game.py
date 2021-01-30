import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
import numpy as np

# fichiers maison
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
    compteur = 0
    delta_t = 150
    while running:

        list_event, list_pressed = pg.event.get(), pg.key.get_pressed()

        if list_pressed[pg.K_UP]:
            has_changed = True
            perso.deplacement((0,-1), mat)
            pg.time.wait(delta_t)
            compteur += 1

        if list_pressed[pg.K_DOWN]:
            has_changed = True
            perso.deplacement((0,1), mat)
            pg.time.wait(delta_t)
            compteur += 1

        if list_pressed[pg.K_RIGHT]:
            has_changed = True
            perso.deplacement((1,0), mat)
            pg.time.wait(delta_t)
            compteur += 1

        if list_pressed[pg.K_LEFT]:
            has_changed = True
            perso.deplacement((-1,0), mat)
            pg.time.wait(delta_t)
            compteur += 1


        for event in list_event:
                if event.type == pg.QUIT:
                    running = False
                    return 2
                elif event.type == pg.KEYDOWN:
                    has_changed = True
                    # compteur += 1

                    if event.key == pg.K_q:
                        running = False
                        return 2

        if has_changed:
            display.affichage(screen, mat, images,perso)
            has_changed = False
            pg.display.update()
        if perso.escalier:
            perso.escalier = False
            return 1 #on va passer au niveau suivant
        if perso.vie == 0:
            return 0 #game_over
        if perso.etat <= 0 or perso.faim <= 0:
            perso.vie -= 1
            perso.faim = perso.FAIM_MAX
            perso.etat = perso.ETAT_MAX
            perso.epee = False
        if compteur == 10:
            compteur = 0
            if perso.etat < perso.ETAT_MAX:
                perso.etat += 1
            perso.faim -= 5
    return 0