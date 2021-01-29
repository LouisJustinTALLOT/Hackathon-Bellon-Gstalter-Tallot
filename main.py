import pygame as pg
from random import randint

import display

# faire 'Q' pour arrêter le script'

pg.init()
n, m = 400, 300
screen = display.init_display(n, m)
clock = pg.time.Clock()
running = True
display.add_borders(screen, n, m)
while running:
    clock.tick(1)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
            if event.key == pg.K_q:
                running = False
    pg.display.update()
pg.quit()