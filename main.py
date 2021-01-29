import pygame as pg
import sys
sys.path.insert(1, './src')

import get_levels
import display
import heros


# faire 'Q' pour arrêter le script'
pg.init()
n, m = 400, 300
screen = display.init(n, m) #appelle le fichier externe display.py
perso = heros.Heros(20,20)
clock = pg.time.Clock()
running = True
images = [pg.image.load("images/sol.png"), pg.image.load("images/heros.png"), pg.image.load("images/mur.png")] #images à afficher
while running:
    clock.tick(1)
    for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    running = False
                if event.key == pg.K_UP:
                    perso.deplacement((0,-16))
                if event.key == pg.K_DOWN:
                    perso.deplacement((0,16))
                if event.key == pg.K_RIGHT:
                    perso.deplacement((16,0))
                if event.key == pg.K_LEFT:
                    perso.deplacement((-16,0))
    perso.affiche_heros(screen)       
    pg.display.update()
pg.quit()