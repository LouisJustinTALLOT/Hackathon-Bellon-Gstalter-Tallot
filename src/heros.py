import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
import sys
import random as rd
sys.path.insert(1, './src')

class Heros:
    """La classe dont le personnage va être une instance"""

    ETAT_MAX = 100
    FAIM_MAX = 100
    
    def __init__(self, x=0, y=0):
        self.x = x                # position en abscisses
        self.y = y                # position en ordonnées
        self.x0, self.y0 = x, y   # les positions initiales pour respawn
        self.vie = 3              # nombre total de vies
        self.etat = self.ETAT_MAX # on initialise l'état initial
        self.faim = self.FAIM_MAX # ainsi que la faim initiale
        self.escalier = False     # variable pour les changements de niveau
        self.epee = False         # le perso peut avoir une épée
        self.clef = False         # une clé
        self.nageur = False       # il peut savoir nager
        self.fusee = 1            # peut aller plus vite avec les fusées
        self.compteur_fusee = 0   # compteur pour la vitesse
        self.score = 0            # le score qui s'accumule
        self.argent = 0           # le porte-monnaie
        self.precedent = 0        # la case où il était précédemment

    def deplacement(self, direction, matrice, liste_monstres):
        """On déplace le personnage dans la direction demandée
        en respectant certaines règles
        """

        x = self.x
        y = self.y
        x += direction[0]
        y += direction[1]

        prochain = matrice[y][x]  # le point où le perso est censé aller

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

        elif prochain in [5, 49, 50]:   # monstre
            monstre : Monstre
            for i, monstre in enumerate(liste_monstres):
                if (monstre.x, monstre.y) == (x, y):
                    if self.epee:
                        matrice[y][x] = 0
                        monstre.etat -= rd.randint(15, 30)
                        monstre.deplacement((0,0), matrice, self)
                        self.etat -= rd.randint(0, 10)
                    else:
                        if not monstre.compteur_attaque:
                            self.etat -= rd.randint(10, 20)
                            monstre.compteur_attaque -= 1
                        monstre.compteur_attaque = 10


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
    """La classe dont les monstres vont être des instances"""

    ETAT_MAX = 20
    # FAIM_MAX = 100    # les monstres n'ont pas faim
    
    def __init__(self, x=0, y=0, aquatique=False, herbeux=False, no=5, niveau=0):
        self.x = x
        self.y = y
        self.x0, self.y0 = x, y # les positions initiales pour respawn
        self.niveau = niveau
        self.vie = 1 # le monstre a une seule vie
        self.etat = self.ETAT_MAX * self.niveau
        # self.faim = self.FAIM_MAX
        # self.escalier = False
        # self.epee = False
        # self.clef = False
        self.nageur = aquatique
        self.herbeux = herbeux
        # self.fusee = 1
        # self.compteur_fusee = 0
        # self.score = 0
        # self.argent = 0
        self.precedent = 0
        self.numero = no
        self.compteur_attaque = 0

    def deplacement(self, direction, matrice, heros:Heros):
        """On déplace les monstres dans la direction demandée
        en suivant les règles applicables
        """

        x = self.x
        y = self.y
        x += direction[0]
        y += direction[1]

        prochain = matrice[y][x]

        if self.etat <= 0:
            self.vie = 0
            heros.score += 30

        if not self.vie:
            matrice[self.y][self.x] = self.precedent

        elif prochain in [2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 48]:     # mur
            # self.etat -= 1
            pass # monstres immortels

        elif prochain == 0:   # sol
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                matrice[y][x] = self.numero
                self.x, self.y = x, y
                self.precedent = 0
        
        elif prochain == 21:   # sol sombre
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                matrice[y][x] = self.numero
                self.x, self.y = x, y
                self.precedent = 21

        elif prochain in [43, 44]:   # glace
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                matrice[y][x] = self.numero
                self.x, self.y = x, y
                self.precedent = prochain
                # pg.time.wait(50)

        elif prochain in [39, 40, 41]: #herbe
            if self.precedent != 20:
                matrice[self.y][self.x] = self.precedent
                matrice[y][x] = self.numero
                self.x, self.y = x, y
                self.precedent = prochain
                

        elif prochain == 6:   # porte
            matrice[self.y][self.x] = self.precedent
            self.x, self.y = x, y
            matrice[self.y][self.x] = self.numero
            self.precedent = 6

        elif prochain == 3:   # escalier
            pass # les monstres ne nous suivent pas au niveau suivant
            # self.escalier = True
            # self.score += 100

        elif prochain == 4:   # pomme
            matrice[self.y][self.x] = 0
            matrice[y][x] = self.numero
            self.x, self.y = x, y
            # self.faim += 10
            # self.score += 5
            self.precedent = 4

        elif prochain in [5, 49]:   # monstre
            pass # pas de combats entre monstres
            # if self.epee:
            #     matrice[y][x] = 0
            #     self.score += 30
            # else:
            #     self.etat -= 20

        elif prochain == 1:   # héros
            if heros.epee:
                self.etat -= rd.randint(15, 30)
                heros.etat -= rd.randint(0, 10)
            else:
                if not self.compteur_attaque:
                    heros.etat -= rd.randint(5, 20)
                    self.compteur_attaque = 10
                self.compteur_attaque -= 1
                

        elif prochain == 7:   # potion
            matrice[self.y][self.x] = 0
            matrice[y][x] = self.numero
            self.x, self.y = x, y
            self.etat += 10
            # self.score += 5
            self.precedent = 7

        elif prochain == 8:   # épée
            matrice[self.y][self.x] = 0
            matrice[y][x] = self.numero
            self.x, self.y = x, y
            # self.epee = True
            # self.score += 50
            self.precedent = 8

        elif prochain == 9:   # or
            matrice[self.y][self.x] = 0
            matrice[y][x] = self.numero
            self.x, self.y = x, y
            # self.score += 20
            # self.argent += rd.randint(1,20)
            self.precedent = 9

        elif prochain == 20:  # couloir
            if self.precedent in [20, 6]:
                matrice[y][x] = self.numero
                matrice[self.y][self.x] = self.precedent
                self.x, self.y = x, y
                self.precedent = 20
            # else:
            #     self.etat -= 1

        elif prochain == 22:   # clé
            matrice[self.y][self.x] = 0
            matrice[y][x] = self.numero
            self.x, self.y = x, y
            # self.clef = True
            # self.score += 10
            self.precedent = 22

        elif prochain == 45 : # coffre
            # si on a la clé, ça ouvre le coffre et il disparaît
            # sinon rien
            pass #les monstres n'ouvrent pas les coffres
            # if self.clef:
            #     # self.score += 100
            #     # self.clef = False
            #     matrice[self.y][self.x] = 0
            #     matrice[y][x] = self.numero
            #     self.x, self.y = x, y
            #     self.precedent = 0
            #     # self.argent += rd.randint(50,150)

        elif prochain == 42:  # fusée
            matrice[self.y][self.x] = 0
            matrice[y][x] = self.numero
            self.x, self.y = x, y
            # self.fusee = 3
            # self.compteur_fusee = 250
            # self.score += 10
            self.precedent = 42

        elif prochain == 47:   # potion pour nager
            matrice[self.y][self.x] = 0
            matrice[y][x] = self.numero
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
                    # self.precedent = 0
                    pass
                else:                
                    self.x, self.y = x, y
                    self.precedent = prochain
                matrice[self.y][self.x] = self.numero



            
    def deplace_vers_heros(self, matrice, heros:Heros, compteur_mvt=0, deja_fait=False):
        """Déplace automatiquement le monstre dans la direction du héros"""
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

        if compteur_mvt:
            self.deplacement((dep_x, 0), matrice, heros)
        else:
            self.deplacement((0, dep_y), matrice, heros)

        if rd.random()>0.6 and not deja_fait:
            self.deplace_vers_heros(matrice, heros, (compteur_mvt+1)%2, True)