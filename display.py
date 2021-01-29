import pygame as pg, sys
from random import randint

def init(n, m):
    screen = init_display(n, m)
    add_borders(screen, n, m)
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
