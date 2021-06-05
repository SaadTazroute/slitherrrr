from math import sqrt
from random import randint

from fltk import *
import fltk


#dimentions = [400, 600]
#h = int(dimentions[0]/50)
#l = int(dimentions[1]/50)

ax = {}
ay = {}
etat = {}

def libre(etat,segment) :
    if segment in list(etat.keys()):
        return False
    return True

def est_interdit(etat,segment) :
    if segment in list(etat.keys()):
        print("Interdit!")

def arete(pt1, pt2, couleure="black", tag=""):
    dist = sqrt( (pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 )
    if dist != 1:
        print("too far")
        return
    #add condition sur
    if len(tag)==0:
        tag = "({},{}),({},{})".format(pt1[0], pt1[1], pt2[0], pt2[1])
    rectangle((pt1[0] * 50) + 3, (pt1[1] * 50) + 3, (pt2[0] * 50) - 3, (pt2[1] * 50) - 3, remplissage=couleure, tag=tag)
    print(tag)


if __name__ == "__main__":
    #l = int(input("largeur : "))
    #h = int(input("hauteur : "))
    l = 7
    h = 6
    dimentions = [l * 50, h * 50]
    #hna koun ghi tzid dik la partie read text
    #bach yloadi l indices
    #khass tkoun l matrice f nfss dim li dkhlna f l w h sinn thet l w h 3la hsab la matrice li athet
    indices = []
    for r in range(h):
        s = []
        for k in range(l):
            s.append(randint(0,3))
        indices.append(s)

    #indices = [[randint(1,9)] * l] * h
    cree_fenetre(dimentions[0]+50, dimentions[1]+50)
    for i in range(int(dimentions[0] / 50)):
        ax[i] = i * 50
    for j in range(int(dimentions[1] / 50)):
        ay[j] = j * 50
    for i in range(int(dimentions[0] / 50)):
        for j in range(int(dimentions[1] / 50)):
            cercle(ax[i]+50, ay[j]+50, 3, remplissage="red")
            if i <((dimentions[0]/50)-1) and j<((dimentions[1]/50)-1):
                #if none:
                #pass
                #else:
                texte(ax[i]+20+50, ay[j]+10+50, str(indices[j][i]), taille=17)
    #image(200, 200, 'red_x.jpg', ancrage='center')
    attend_ev()
    # Boucle du jeu
    while True:
        ev = donne_ev()
        tev = type_ev(ev)

        # Action dépendant du type d'événement reçu :

        if tev == 'Touche':
            print('Appui sur la touche', touche(ev))

        elif tev == "ClicDroit":
            # need to add a condition to stay in the game field(la brkti 3liiiimn ga3 wla 3liisr ga3 wakha machi bin 2 points rah ayrsmolk)
            if (abscisse(ev) + 3) % 50 <= 6 :
                if libre(etat, ((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)), (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))):
                    arete([int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)],
                          [int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1], "black")
                    etat[((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)),
                          (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))] = 1
                    print(etat)
                    # test si l'action est permise ou pas
                    # si permise: pass
                    # si interdit: change all colors to red and maybe raise game over
                else:
                    pt1_eff = [int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)]
                    pt2_eff = [int((abscisse(ev) + 3) / 50) , int((ordonnee(ev)) / 50) + 1]
                    efface("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    print("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    del etat[((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)), (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))]
                    print(etat)
                    print("effacé")
                    mise_a_jour()

            if (ordonnee(ev) + 3) % 50 <= 6:
                if libre(etat, ((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                                (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))):
                    arete([int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)],
                          [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)], "black")
                    etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                          (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))] = 1
                    print(etat)
                    # test si l'action est permise ou pas
                    # si permise: pass
                    # si interdit: change all colors to red and maybe raise game over
                else:
                    pt1_eff=[int((abscisse(ev)) / 50),
                                         int((ordonnee(ev) + 3) / 50)]
                    pt2_eff = [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)]
                    print("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    efface("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    del etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)), (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))]
                    print("effacé")
                    print(etat)
                    attend_ev()

        elif tev == "ClicGauche":
            if (abscisse(ev) + 3) % 50 <= 6:
                if libre(etat, ((int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)),
                                (int((abscisse(ev) + 3) / 50), int((ordonnee(ev) / 50)) + 1))):
                    arete([int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)],
                              [int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50) + 1], "red")
                    etat[((int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)),
                              (int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50) + 1))] = -1
                    print(etat)
                    # test si l'action est permise ou pas
                    # si permise: pass
                    # si interdit: change all colors to red and maybe raise game over
                else:
                    pt1_eff = [int((abscisse(ev) + 3) / 50),
                               int((ordonnee(ev)) / 50)]
                    pt2_eff = [int((abscisse(ev) + 3) / 50), int((ordonnee(ev) / 50)) + 1]
                    print("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    efface("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    del etat[((pt1_eff[0], pt1_eff[1]), (pt2_eff[0], pt2_eff[1]))]
                    print("effacé")
                    print(etat)
                    attend_ev()
            if (ordonnee(ev) + 3) % 50 <= 6:
                if libre(etat, ((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                      (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))):
                    arete([int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)],
                          [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)], "red")
                    etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                          (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))] = -1
                    print(etat)
                    # test si l'action est permise ou pas
                    # si permise: pass
                    # si interdit: change all colors to red and maybe raise game over
                else:
                    pt1_eff = [int((abscisse(ev)) / 50),
                               int((ordonnee(ev) + 3) / 50)]
                    pt2_eff = [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)]
                    print("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    efface("({},{}),({},{})".format(pt1_eff[0], pt1_eff[1], pt2_eff[0], pt2_eff[1]))
                    del etat[((pt1_eff[0], pt1_eff[1]), (pt2_eff[0], pt2_eff[1]))]
                    print("effacé")
                    print(etat)
                    attend_ev()

        elif tev == 'Quitte':  # on sort de la boucle
            break

        else:  # dans les autres cas, on ne fait rien
            pass

        mise_a_jour()
    ferme_fenetre()
