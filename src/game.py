import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
import numpy as np

# fichiers maison
import src.get_levels as gl
import src.display as display
import src.heros as heros

def init_level(list_levels, i):
    """Initialise les variables au début d'un niveau"""
    level = list_levels[i]
    mat = level.matrice_niveau
    bool_matrice = np.ones((len(mat), len(mat[0])))
    x0, y0 = level.depart_heros_x, level.depart_heros_y

    # on va chercher les différents monstres présents sur la carte
    liste_monstres = []
    n, m = len(mat), len(mat[0])
    # n hauteur, m longueur
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 5 : # on pourra étendre
                liste_monstres.append(heros.Monstre(j, i))
            if mat[i][j] == 49:
                liste_monstres.append(heros.Monstre(j, i, aquatique=True, no=49))
            if mat[i][j] == 50:
                liste_monstres.append(heros.Monstre(j, i, herbeux=True, no=50))


                
    return mat, x0, y0, liste_monstres

def play_game(screen, perso:heros.Heros, mat, images, liste_monstres=[]):
    """Joue un niveau du jeu jusqu'à la mort ou au niveau suivant"""
    running = True
    has_changed = False
    compteur = 0
    delta_t = 100
    increment_aleatoire = 0
    increment_aleatoire_2 = 0
    increment_aleatoire_3 = 0
    compteur_mvt = 0

    while running:
        # la boucle qui tourne dans tout le niveau
        list_event, list_pressed = pg.event.get(), pg.key.get_pressed()

        # on déplace selon les touches pressées
        if list_pressed[pg.K_UP]:
            has_changed = True
            perso.deplacement((0,-1), mat, liste_monstres)
            compteur += 1

        if list_pressed[pg.K_DOWN]:
            has_changed = True
            perso.deplacement((0,1), mat, liste_monstres)
            compteur += 1

        if list_pressed[pg.K_RIGHT]:
            has_changed = True
            perso.deplacement((1,0), mat, liste_monstres)
            compteur += 1

        if list_pressed[pg.K_LEFT]:
            has_changed = True
            perso.deplacement((-1,0), mat, liste_monstres)
            compteur += 1


        for event in list_event:
            # les conditions d'arrêt
                if event.type == pg.QUIT:
                    running = False
                    return 2
                elif event.type == pg.KEYDOWN:
                    has_changed = True
                    # compteur += 1

                    if event.key == pg.K_q:
                        running = False
                        return 2
 
        # ici, on fait bouger l'herbe, l'eau.....
        increment_aleatoire = (increment_aleatoire + 1 )%2
        increment_aleatoire_2 = (increment_aleatoire_2 + 1) %5
        increment_aleatoire_3 = (increment_aleatoire_3 + 1) %20
        n, m = len(mat), len(mat[0])
        # n hauteur, m longueur
        for i in range(n):
            for j in range(m):
                case = mat[i][j]
                if case in [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]:
                    case += (increment_aleatoire==0)
                    if case > 38:
                        case = 23
                
                elif case in [39, 40, 41]:
                    case += (increment_aleatoire_2==0)
                    if case > 41:
                        case = 39

                elif case in [43, 44]:
                    case += (increment_aleatoire_2==0)
                    if case > 44:
                        case = 43

                mat[i][j] = case

        if has_changed or increment_aleatoire :
            display.affichage(screen, mat, images, perso)
            pg.display.update()
            if perso.fusee == 3:
                perso.compteur_fusee -= 1
                if perso.compteur_fusee == 0:
                    perso.fusee = 1
        pg.time.wait(delta_t//perso.fusee)

        if has_changed:
            # le personnage a alors bougé
            has_changed = False
            # puis on déplace les monstres
            monstre : heros.Monstre
            compteur_mvt = (compteur_mvt+1)%2
            for monstre in liste_monstres :
                monstre.deplace_vers_heros(mat, perso, compteur_mvt)
            
        if perso.escalier:
            # on va passer au niveau suivant
            perso.escalier = False
            return 1 

        if perso.vie == 0:
            # game_over
            return 0 

        if perso.etat <= 0 or perso.faim <= 0:
            # on lui fait alors perdre une vie 
            # et revenir au point de spawn du niveau
            perso.vie -= 1
            perso.faim = perso.FAIM_MAX
            perso.etat = perso.ETAT_MAX
            perso.epee = False
            perso.clef = False
            perso.fusee = 1
            perso.nageur = False
            compteur = 0
            mat[perso.y][perso.x] = perso.precedent
            perso.x, perso.y = perso.x0, perso.y0
            mat[perso.y][perso.x] = 1
            
            # pg.time.wait(1000)

        if compteur == 15:
            compteur = 0
            if perso.etat < perso.ETAT_MAX:
                perso.etat += 1
            perso.faim -= 5
    return 0