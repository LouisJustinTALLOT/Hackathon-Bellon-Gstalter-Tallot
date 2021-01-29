# modules
import pygame as pg

# fichiers maisons
import src.get_levels as gl
import src.display as display
import src.heros as heros


# faire 'Q' pour arrêter le script'
list_levels = gl.load_all_levels()
mat = list_levels[0].matrice_niveau
pg.init()
n, m = len(mat), len(mat[0])
screen = display.init(m, n) #appelle le fichier externe display.py
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
                    perso.deplacement((0,-1), mat)
                if event.key == pg.K_DOWN:
                    perso.deplacement((0,1), mat)
                if event.key == pg.K_RIGHT:
                    perso.deplacement((1,0), mat)
                if event.key == pg.K_LEFT:
                    perso.deplacement((-1,0), mat)
    display.affichage(screen, mat, images)
    pg.display.update()
pg.quit()