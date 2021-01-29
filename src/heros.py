import pygame as pg
import sys
sys.path.insert(1, './src')

class Heros:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.vie = 3
        self.etat = 100
        self.faim = 100


    # def affiche_heros(self, screen):
    #     rect = pg.Rect(self.x, self.y, self.width, self.height)
    #     color = (0, 0, 255) 
    #     pg.draw.rect(screen, color, rect)
    
    def deplacement(self, direction, matrice):
        x = self.x
        y = self.y
        x += direction[0]
        y += direction[1]
        if matrice[y][x] == 2:    # mur
            self.etat -= 1

        elif matrice[y][x] == 0:  # sol
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y

        elif matrice[y][x] == 6:   # porte
            matrice[self.y][self.x] = 0
            self.x, self.y = x + direction[0], y + direction[1]
            matrice[self.y][self.x] = 1

        elif matrice[y][x] == 3:   # escalier
            pass
            #changement de niveau

        elif matrice[y][x] == 4:   # pomme
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.faim += 10

        elif matrice[y][x] == 5:   # monstre
            self.etat -= 20  

        elif matrice[y][x] == 7:   # potion
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.etat += 10



# section de test 

if __name__ == "__main__":
    pass

