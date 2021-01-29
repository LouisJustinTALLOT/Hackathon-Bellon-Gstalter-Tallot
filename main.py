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
          pg.image.load("images/potion.png")
] #images à afficher

condition = True
ct = 0 #compteur pour les différents niveaux
while condition: #on évolue niveau par niveau
    mat, x0, y0 = game.init_level(list_levels, ct)
    perso = heros.Heros(x0, y0)
    n, m = len(mat), len(mat[0])
    screen = display.init(m, n)
    p = game.play_game(screen, perso, mat, images)
    if p == 0: #game_over
        break
    ct += 1
pg.quit()