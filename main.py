# modules
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg

# fichiers maisons
import src.get_levels as gl
import src.display as display
import src.heros as heros
import src.game as game

# Initialisation
list_levels = gl.load_all_levels()
pg.init()
pg.display.set_caption('Rogue')
clock = pg.time.Clock()
images = [pg.image.load("images/sol.png"), 
          pg.image.load("images/heros.png"), 
          pg.image.load("images/mur.png"),
          pg.image.load("images/escalier.png"),
          pg.image.load("images/pomme.png"),
          pg.image.load("images/monstre.png"),
          pg.image.load("images/porte.png"),
          pg.image.load("images/potion.png"),
          pg.image.load("images/epee.png"),
          pg.image.load("images/dollar.png"),
          pg.image.load("images/mur_coin_haut_droit.png"),
          pg.image.load("images/mur_coin_haut_gauche.png"),
          pg.image.load("images/mur_coin_bas_gauche.png"),
          pg.image.load("images/mur_coin_bas_droit.png"),
          pg.image.load("images/mur_T_normal.png"),
          pg.image.load("images/mur_T_inv.png"),
          pg.image.load("images/mur_T_droit.png"),
          pg.image.load("images/mur_T_gauche.png"), 
          pg.image.load("images/mur_horizontal.png"), 
          pg.image.load("images/mur_vertical.png"),
          pg.image.load("images/couloir.png"),
          pg.image.load("images/noir.png")
] #images à afficher
messages = [pg.image.load("images/perdu.png"),
            pg.image.load("images/bravo.png"),
            pg.image.load("images/seeya.png")
] #bravo et perdu

condition = True
ct = 0 #compteur pour les différents niveaux
longueur = len(list_levels)
mat, x0, y0 = game.init_level(list_levels, ct)
perso = heros.Heros(x0, y0)
while condition: #on évolue niveau par niveau
    mat, x0, y0 = game.init_level(list_levels, ct)
    perso.x, perso.y = x0, y0
    n, m = len(mat), len(mat[0])
    screen = display.init(m, n)
    p = game.play_game(screen, perso, mat, images)

    if p == 0: #game_over
        display.gagne_ou_perdu(screen, messages, 0, perso)
        pg.display.update()
        break
    if p == 2:
        display.gagne_ou_perdu(screen, messages, 2, perso)
        pg.display.update()
        break

    ct += 1 #on va lancer le niveau suivant
    if ct == longueur:
        display.gagne_ou_perdu(screen, messages, 1, perso)
        pg.display.update()
        break
pg.time.wait(5000)
pg.quit()
