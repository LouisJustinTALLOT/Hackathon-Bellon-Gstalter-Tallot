import pygame as pg

class Heros:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 16 # largeur du heros en pixels
        self.height = 16 # hauteur du heros en pixels
        self.vie = 3

    def affiche_heros(self, screen):
        rect = pg.Rect(self.x, self.y, self.width, self.height)
        color = (0, 0, 255) 
        pg.draw.rect(screen, color, rect)
    
    def deplacement(self, direction):
        self.x += direction[0]
        self.y += direction[1]





if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((400, 300))
    perso = Heros(20,20)
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
        perso.affiche_heros(screen)
        perso.deplacement((0,20))
        pg.display.update()

