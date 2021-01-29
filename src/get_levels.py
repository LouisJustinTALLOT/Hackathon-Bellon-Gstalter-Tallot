import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

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



    return 0


class Level:

    def __init__(self, no=1, long=0, height=0) -> None:
        self.numero = no
        self.longueur = long
        self.hauteur = height


    def load_from_txt(self, path:str):
        # print("path : ", path, "\n")
        with open(path, 'r', encoding='utf8') as file:
            tableau_niveau = file.readlines()
            print(tableau_niveau)


def load_all_levels():
    """ Retourne un tableau contenant des instances de Level
    à partir des fichiers présents dans /levels
    """

    list_levels = []

    # on récupère le chemin du fichier
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # print(dir_path, end="\n\n")
    # os.chdir(dir_path)
    # on se place dans le répertoire principal
    os.chdir(os.path.pardir)
    os.chdir("levels") # on est dans le dossier des niveaux
    
    liste_des_fichiers = os.listdir() # tous les fichiers de niveaux
    liste_des_fichiers.sort()
    i = 0

    for fi in liste_des_fichiers:
        i += 1 
        niveau = Level(no=i)
        niveau.load_from_txt(fi)

        list_levels.append(niveau)

    return list_levels
        


if __name__ == "__main__":
    """ la section de tests du module"""
   
    ######
    # a = tableau_vide(3,4)
    # print(a)
    # a[2][1] = 3
    # print(a)
    ###################################

    list_levels = load_all_levels()

    print("\n______________________________________")
    for ligne in list_levels[0].matrice_niveau:
        for i in ligne:
            if i:
                print(i, end="")
            else:
                print(" ", end="")
        print("")

