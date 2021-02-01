import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
import sys
import random as rd
sys.path.insert(1, './src')

class Heros:
    ETAT_MAX = 100
    FAIM_MAX = 100
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.x0, self.y0 = x, y # les positions initiales pour respawn
        self.vie = 3
        self.etat = self.ETAT_MAX
        self.faim = self.FAIM_MAX
        self.escalier = False
        self.epee = False
        self.clef = False
        self.nageur = False
        self.fusee = 1
        self.compteur_fusee = 0
        self.score = 0
        self.argent = 0
        self.precedent = 0

    def deplacement(self, direction, matrice, liste_monstres):
        x = self.x
        y = self.y
        x += direction[0]
        y += direction[1]

        prochain = matrice[y][x]

        if prochain in [2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 48]:     # mur
            self.etat -= 1

        elif prochain == 0:   # sol
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                matrice[y][x] = 1
                self.x, self.y = x, y
                self.precedent = 0
        
        elif prochain == 21:   # sol sombre
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                matrice[y][x] = 1
                self.x, self.y = x, y
                self.precedent = 21

        elif prochain in [43, 44]:   # glace
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                matrice[y][x] = 1
                self.x, self.y = x, y
                self.precedent = prochain
                pg.time.wait(50)

        elif prochain == 6:   # porte
            matrice[self.y][self.x] = self.precedent
            self.x, self.y = x, y
            matrice[self.y][self.x] = 1
            self.precedent = 6

        elif prochain == 3:   # escalier
            self.escalier = True
            self.score += 100

        elif prochain == 4:   # pomme
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.faim += 10
            self.score += 5

        elif prochain == 5:   # monstre
            monstre : Monstre
            for i, monstre in enumerate(liste_monstres):
                if (monstre.x, monstre.y) == (x, y):
                    break
            if self.epee:
                matrice[y][x] = 0
                self.score += 30
                liste_monstres[i].vie = 0
            else:
                self.etat -= 20

        elif prochain == 7:   # potion
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.etat += 10
            self.score += 5
            self.precedent = 0

        elif prochain == 8:   # épée
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.epee = True
            self.score += 50
            self.precedent = 0

        elif prochain == 9:   # or
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.score += 20
            self.argent += rd.randint(1,20)
            self.precedent = 0

        elif prochain == 20:  # couloir
            if self.precedent in [20, 6]:
                matrice[y][x] = 1
                matrice[self.y][self.x] = self.precedent
                self.x, self.y = x, y
                self.precedent = 20
            else:
                self.etat -= 1

        elif prochain == 22:   # clé
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.clef = True
            self.score += 10
            self.precedent = 0

        elif prochain == 45 : # coffre
            # si on a la clé, ça ouvre le coffre et il disparaît
            # sinon rien
            if self.clef:
                self.score += 100
                self.clef = False
                # matrice[self.y][self.x] = 0
                matrice[y][x] = 0
                # self.x, self.y = x, y
                # self.precedent = 0
                self.argent += rd.randint(50,150)

        elif prochain == 42:  # fusée
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.fusee = 3
            self.compteur_fusee = 250
            self.score += 10
            self.precedent = 0

        elif prochain == 47:   # potion pour nager
            matrice[self.y][self.x] = 0
            matrice[y][x] = 1
            self.x, self.y = x, y
            self.nageur = True
            self.score += 10
            self.precedent = 0

        elif prochain in [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]: # eau
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                if not self.nageur:
                    self.etat -= 2*self.ETAT_MAX    # 2* sinon si on a pris la potion juste avant il se noie mais perd pas de vie...
                    self.x, self.y = self.x0, self.y0
                    self.precedent = 0
                else:                
                    self.x, self.y = x, y
                    self.precedent = prochain
                matrice[self.y][self.x] = 1
            

class Monstre:
    ETAT_MAX = 100
    FAIM_MAX = 100
    
    def __init__(self, x=0, y=0, aquatique=False):
        self.x = x
        self.y = y
        self.x0, self.y0 = x, y # les positions initiales pour respawn
        self.vie = 3
        self.etat = self.ETAT_MAX
        self.faim = self.FAIM_MAX
        self.escalier = False
        self.epee = False
        self.clef = False
        self.nageur = aquatique
        self.fusee = 1
        self.compteur_fusee = 0
        self.score = 0
        self.argent = 0
        self.precedent = 0

    def deplacement(self, direction, matrice):
        x = self.x
        y = self.y
        x += direction[0]
        y += direction[1]

        prochain = matrice[y][x]

        if not self.vie:
            return

        elif prochain in [2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 48]:     # mur
            # self.etat -= 1
            pass # monstres immortels

        elif prochain == 0:   # sol
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                matrice[y][x] = 5
                self.x, self.y = x, y
                self.precedent = 0
        
        elif prochain == 21:   # sol sombre
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                matrice[y][x] = 5
                self.x, self.y = x, y
                self.precedent = 21

        elif prochain in [43, 44]:   # glace
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                matrice[y][x] = 5
                self.x, self.y = x, y
                self.precedent = prochain
                # pg.time.wait(50)

        elif prochain == 6:   # porte
            matrice[self.y][self.x] = self.precedent
            self.x, self.y = x, y
            matrice[self.y][self.x] = 5
            self.precedent = 6

        elif prochain == 3:   # escalier
            pass # les monstres ne nous suivent pas au niveau suivant
            # self.escalier = True
            # self.score += 100

        elif prochain == 4:   # pomme
            matrice[self.y][self.x] = 0
            matrice[y][x] = 5
            self.x, self.y = x, y
            # self.faim += 10
            # self.score += 5
            self.precedent = 4

        elif prochain == 5:   # monstre
            pass # pas de combats entre monstres
            # if self.epee:
            #     matrice[y][x] = 0
            #     self.score += 30
            # else:
            #     self.etat -= 20

        elif prochain == 7:   # potion
            matrice[self.y][self.x] = 0
            matrice[y][x] = 5
            self.x, self.y = x, y
            self.etat += 10
            # self.score += 5
            self.precedent = 7

        elif prochain == 8:   # épée
            matrice[self.y][self.x] = 0
            matrice[y][x] = 5
            self.x, self.y = x, y
            # self.epee = True
            # self.score += 50
            self.precedent = 8

        elif prochain == 9:   # or
            matrice[self.y][self.x] = 0
            matrice[y][x] = 5
            self.x, self.y = x, y
            # self.score += 20
            # self.argent += rd.randint(1,20)
            self.precedent = 9

        elif prochain == 20:  # couloir
            if self.precedent in [20, 6]:
                matrice[y][x] = 5
                matrice[self.y][self.x] = self.precedent
                self.x, self.y = x, y
                self.precedent = 20
            # else:
            #     self.etat -= 1

        elif prochain == 22:   # clé
            matrice[self.y][self.x] = 0
            matrice[y][x] = 5
            self.x, self.y = x, y
            # self.clef = True
            # self.score += 10
            self.precedent = 22

        elif prochain == 45 : # coffre
            # si on a la clé, ça ouvre le coffre et il disparaît
            # sinon rien
            if self.clef:
                # self.score += 100
                # self.clef = False
                matrice[self.y][self.x] = 0
                matrice[y][x] = 5
                self.x, self.y = x, y
                self.precedent = 0
                # self.argent += rd.randint(50,150)

        elif prochain == 42:  # fusée
            matrice[self.y][self.x] = 0
            matrice[y][x] = 5
            self.x, self.y = x, y
            # self.fusee = 3
            # self.compteur_fusee = 250
            # self.score += 10
            self.precedent = 42

        elif prochain == 47:   # potion pour nager
            matrice[self.y][self.x] = 0
            matrice[y][x] = 5
            self.x, self.y = x, y
            # self.nageur = True
            # self.score += 10
            self.precedent = 47

        elif prochain in [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]: # eau
            # pass # pour l'instant, les monstres ne vont pas dans l'eau
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                if not self.nageur:
                    # self.etat -= 2*self.ETAT_MAX    # 2* sinon si on a pris la potion juste avant il se noie mais perd pas de vie...
                    # self.x, self.y = self.x0, self.y0
                    self.precedent = 0
                else:                
                    self.x, self.y = x, y
                    self.precedent = prochain
                matrice[self.y][self.x] = 5
            
    def deplace_vers_heros(self,matrice, heros:Heros):
        # on a x, y du heros
        # on détermine vers où il est par rapport à nous
        # et on bouge dans cette direction
        delta_x = -(self.x-heros.x)
        delta_y = -(self.y-heros.y)

        if delta_x:
            dep_x = delta_x//abs(delta_x)
        else:
            dep_x = 0

        if delta_y:
            dep_y = delta_y//abs(delta_y)
        else:
            dep_y = 0 
        self.deplacement((dep_x, dep_y), matrice)