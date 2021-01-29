import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

def tableau_vide(n,m):
    return [[0 for j in range(m)] for i in range(n)]

class Level:

    def __init__(self, no=1, long=0, larg=0) -> None:
        self.numero = no
        self.longueur = long
        self.largeur = larg

