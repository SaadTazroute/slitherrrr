from fltk import *
from utilities import *
import os
dimentions = [400, 400]



#indices = chargegrille('grille1.txt')

indices =[[0]*8]*8

ax = {}
etat = {}

def libre(etat,segment) :
    if segment in list(etat.keys()):
        return False
    return True

def est_interdit(etat,segment) :
    if segment in list(etat.keys()):
        print("Interdit!")


def arete(pt1, pt2, couleure="black", tag=""):
    if pt1[0] != pt2[0] and pt1[1] != pt2[1]:
        return
    #add condition sur
    if len(tag)==0:
        tag = "({},{}),({},{})".format(pt1[0],pt1[1],pt2[0], pt2[1])
    rectangle((pt1[0] * 50) + 3, (pt1[1] * 50) + 3, (pt2[0] * 50) - 3, (pt2[1] * 50) - 3, remplissage=couleure, tag=tag)
    print(tag)


if __name__ == "__main__":
    cree_fenetre(400, 400)
    for i in range(int(dimentions[0] / 50)+1):
        ax[i] = i * 50

    for i in range(int(dimentions[0] / 50)+1):
        for j in range(int(dimentions[0] / 50) + 1):
            cercle(ax[i], ax[j], 3, remplissage="red")
            if i <8 and j<8:
                texte(ax[i]+20, ax[j]+10, str(indices[i][j]), taille=17)

    arete([2, 3], [2, 4], tag="test")

    arete([3, 3], [3, 4], tag="test")
    attend_ev()
    efface("test")
    attend_ev()

    while True:
        ev = donne_ev()
        tev = type_ev(ev)

        # Action dépendant du type d'événement reçu :

        if tev == 'Touche':
            print('Appui sur la touche', touche(ev))

        elif tev == "ClicDroit":
            if abscisse(ev) % 50 <=3:
                if libre(etat, ((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)), (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))):
                    arete([int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)],
                          [int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1], "blue")
                    etat[((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)),
                          (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))] = 1
                    print(etat)
                else:
                    pt1_eff=[int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)]
                    pt2_eff=[int((abscisse(ev) + 3) / 50) , int((ordonnee(ev)) / 50) + 1]
                    efface("({},{}),({},{})".format(pt1_eff[0],pt1_eff[1],pt2_eff[0], pt2_eff[1]))
                    mise_a_jour()
                    print("effacé")
                    print("({},{}),({},{})".format(pt1_eff[0],pt1_eff[1],pt2_eff[0], pt2_eff[1]))
                    del etat[((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)), (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))]
                    print(etat)
            if ordonnee(ev) % 50 <= 3:
                if libre(etat, ((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                                (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))):
                    arete([int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)],
                          [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)], "black")
                    etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                          (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))] = 1
                else:
                    pt1_eff=[int((abscisse(ev)) / 50),
                                         int((ordonnee(ev) + 3) / 50)]
                    pt2_eff = [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)]
                    print("({},{}),({},{})".format(pt1_eff[0],pt1_eff[1],pt2_eff[0], pt2_eff[1]))
                    efface("({},{}),({},{})".format(pt1_eff[0],pt1_eff[1],pt2_eff[0], pt2_eff[1]))
                    del etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)), (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))]
                    print("effacé")
                    attend_ev()

        elif tev == "ClicGauche":
            if abscisse(ev) % 50 <= 3:
                arete([int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)],
                      [int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50) + 1], "red")
                etat[((int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)),
                      (int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50) + 1))] = -1
                print(etat)
            #same as above
            if ordonnee(ev) % 50 <= 3:
                arete([int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)],
                      [int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)], "red")
                etat[((int((abscisse(ev)) / 50), int((ordonnee(ev) + 3) / 50)),
                      (int((abscisse(ev)) / 50) + 1, int((ordonnee(ev) + 3) / 50)))] = -1
            # same as above

        elif tev == 'Quitte':  # on sort de la boucle
            break

        else:  # dans les autres cas, on ne fait rien
            pass

        mise_a_jour()
    ferme_fenetre()