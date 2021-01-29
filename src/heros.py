import pygame as pg
import sys
sys.path.insert(1, './src')

class Heros:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.vie = 3
        self.etat = 100

    # def affiche_heros(self, screen):
    #     rect = pg.Rect(self.x, self.y, self.width, self.height)
    #     color = (0, 0, 255) 
    #     pg.draw.rect(screen, color, rect)
    
    def deplacement(self, direction, matrice):
        x = self.x
        y = self.y
        x += direction[0]
        y += direction[1]
        if matrice[y][x] == 2:
            self.etat -= 1
        if matrice[y][x] == 0:
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
        if matrice[y][x] == 3:
            matrice = 



# section de test 

if __name__ == "__main__":
    pass

