# modules
import pygame as pg
from pygame.constants import CONTROLLER_AXIS_TRIGGERLEFT

# fichiers maisons
import src.get_levels as gl
import src.display as display
import src.heros as heros
import src.game as game

# Initialisation
list_levels = gl.load_all_levels()
pg.init()
clock = pg.time.Clock()
images = [pg.image.load("images/sol.png"), 
          pg.image.load("images/heros.png"), 
          pg.image.load("images/mur.png"),
          pg.image.load("images/escalier.png"),
          pg.image.load("images/pomme.png"),
          pg.image.load("images/monstre.png"),
          pg.image.load("images/porte.png"),
          pg.image.load("images/potion.png"),
          pg.image.load("images/epee.png")
] #images à afficher
messages = [pg.image.load("images/perdu.png"),
            pg.image.load("images/bravo.png")
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
        display.gagne_ou_perdu(screen, messages, 0)
        pg.display.update()
        break
    ct += 1 #on va lancer le niveau suivant
    if ct == longueur:
        display.gagne_ou_perdu(screen, messages, 1)
        pg.display.update()
        break
pg.time.wait(5000)
pg.quit()
