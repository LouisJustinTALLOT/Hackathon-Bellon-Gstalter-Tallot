import os
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))

def tableau_vide(n,m):
    return [[0 for j in range(m)] for i in range(n)]

def interpretation(car):
    """ la fonction qui prend un caractère du niveau en .txt
    et renvoie un entier en fonction du type représenté par
    ce caractère
    """

    if car == " ":
        return 0

    if car == "@":
        return 1

    if car == "#":
        return 2

    if car == 'E': #escalier
        return 3

    if car == 'o': #nourriture
        return 4

    if car == 'M': #monstre
        return 5

    if car == "P": # porte
        return 6

    if car == "h": #potion (healing)
        return 7

    if car == "!":
        return 8

    if car == "$":
        return 9

    if car == "L":
        return 10

    if car == "/":
        return 11

    if car == "]":
        return 12

    if car == "[":
        return 13

    if car == "T":
        return 14

    if car == "t":
        return 15

    if car == "{":
        return 16

    if car == "}":
        return 17

    if car == "-":
        return 18

    if car == "|":
        return 19

    if car == "&":
        return 20

    if car == "_":
        return 21

    if car == "c":
        return 22

    if car == "~":
        return 23
    
    if car == ":":
        return 39
    
    if car == ">":
        return 42

    if car == "g":
        return 43

    return 0

class Level:

    def __init__(self, no=1, long=0, height=0) -> None:
        self.numero = no
        self.longueur = long
        self.hauteur = height
        self.depart_heros_x,self.depart_heros_y = 2,2

    def load_from_txt(self, path:str):
        # print("path : ", path, "\n")
        with open(path, 'r', encoding='utf8') as file:
            tableau_niveau = file.readlines()

        for i, ligne in enumerate(tableau_niveau) :
            # print(repr(ligne))
            if ligne[-1]=="\n":
                tableau_niveau[i] = ligne[:-1] # on fait juste ça pour enlever le \n à la fin de la ligne

        self.longueur = len(tableau_niveau[0])
        self.hauteur = len(tableau_niveau)

        self.matrice_niveau = tableau_vide(self.hauteur, self.longueur)

        for i in range(self.hauteur):
            for j in range(self.longueur):
                car = tableau_niveau[i][j]
                self.matrice_niveau[i][j] = interpretation(car)
                if car == "@":
                    self.depart_heros_x,self.depart_heros_y = j, i


def load_all_levels():
    """ Retourne un tableau contenant des instances de Level
    à partir des fichiers présents dans /levels
    """
    list_levels = []
    liste_des_fichiers = os.listdir("levels") # tous les fichiers de niveaux
    liste_des_fichiers.sort()
    i = 0

    for fi in liste_des_fichiers:
        i += 1
        niveau = Level(no=i)
        niveau.load_from_txt("levels/"+fi)

        list_levels.append(niveau)

    return list_levels





# section de test

if __name__ == "__main__":
    """ la section de tests du module"""

    print(os.path.dirname(os.path.realpath(__file__)))

    ######
    # a = tableau_vide(3,4)
    # print(a)
    # a[2][1] = 3
    # print(a)
    ###################################

    list_levels = load_all_levels()
    print(os.path.dirname(os.path.realpath(__file__)))

    print("\n______________________________________")
    for ligne in list_levels[0].matrice_niveau:
        for i in ligne:
            if i:
                print(i, end="")
            else:
                print(" ", end="")
        print("")

