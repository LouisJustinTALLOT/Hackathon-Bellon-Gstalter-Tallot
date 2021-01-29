import pygame as pg
# import sys
# sys.path.insert(1, './src')

import src.get_levels as gl
import src.display as display
import src.heros as heros


# faire 'Q' pour arrêter le script'
pg.init()
n, m = 40, 30
screen = display.init(n, m) #appelle le fichier externe display.py
perso = heros.Heros(20,20)
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