import pygame as pg

class Heros:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        #self.width = 16 # largeur du heros en pixels
        #self.height = 16 # hauteur du heros en pixels
        self.vie = 3
        self.etat = 100

    # def affiche_heros(self, screen):
    #     rect = pg.Rect(self.x, self.y, self.width, self.height)
    #     color = (0, 0, 255) 
    #     pg.draw.rect(screen, color, rect)
    
    def deplacement(self, direction, matrice):
        if matrice[self.y][self.x] == 2:
            self.etat -= 1
        if matrice[self.y][self.x] == 2:
            matrice[self.x][self.y] = 0
            self.x += direction[0]
            self.y += direction[1]
            matrice[self.y][self.x] = 1




if __name__ == "__main__":
    pass

