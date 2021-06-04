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

    if pt1[0] != pt2[0] and pt1[1] != pt2[1]:
        return
    #add condition sur
    if len(tag)==0:
        tag = "({},{}),({},{})".format(pt1[0],pt1[1],pt2[0], pt2[1])
    rectangle((pt1[0] * 50) + 3, (pt1[1] * 50) + 3, (pt2[0] * 50) - 3, (pt2[1] * 50) - 3, remplissage=couleure, tag=tag)
    print(tag)


if __name__ == "__main__":
    l = int(input("largeur : "))
    h = int(input("hauteur : "))
    dimentions = [l * 50, h * 50]
    #hna koun ghi tzid dik la partie read text
    #bach yloadi l indices
    #khass tkoun l matrice f nfss dim li dkhlna f l w h
    indices = [[1] * l] * h
    cree_fenetre(dimentions[0]+50, dimentions[1]+50)
    for i in range(int(dimentions[0] / 50)):
        ax[i] = i * 50
    for j in range(int(dimentions[1] / 50)):
        ay[j] = j * 50
    for i in range(int(dimentions[0] / 50)):
        for j in range(int(dimentions[1] / 50)):
            cercle(ax[i]+50, ay[j]+50, 3, remplissage="red")
            if i <((dimentions[0]/50)-1) and j<((dimentions[1]/50)-1):
                try :
                    texte(ax[i]+20+50, ay[j]+10+50, str(indices[j][i]), taille=17)
                except:
                    print("fdf")
    attend_ev()

    while True:
        ev = donne_ev()
        tev = type_ev(ev)

        # Action dépendant du type d'événement reçu :

        if tev == 'Touche':
            print('Appui sur la touche', touche(ev))

        elif tev == "ClicDroit":
            # need to add a condition to stay in the game field(la brkto 3liiiimn ga3 wla 3liisr ga3 wakha machi bin 2 points rah ayrsmolk)
            if abscisse(ev) % 50 <=3:
                if libre(etat, ((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)), (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))):
                    arete([int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)],
                          [int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1], "black")
                    etat[((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)),
                          (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))] = 1
                    print(etat)
                else:
                    pt1_eff=[int((abscisse(ev) + 3) / 50), int((ordonnee(ev)) / 50)]
                    pt2_eff=[int((abscisse(ev) + 3) / 50) , int((ordonnee(ev)) / 50) + 1]
                    efface("({},{}),({},{})".format(pt1_eff[0],pt1_eff[1],pt2_eff[0], pt2_eff[1]))
                    print("({},{}),({},{})".format(pt1_eff[0],pt1_eff[1],pt2_eff[0], pt2_eff[1]))
                    del etat[((int((abscisse(ev)+3)/50), int((ordonnee(ev))/50)), (int((abscisse(ev)+3)/50), int((ordonnee(ev))/50) + 1))]
                    print(etat)
                    print("effacé")
                    mise_a_jour()
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
