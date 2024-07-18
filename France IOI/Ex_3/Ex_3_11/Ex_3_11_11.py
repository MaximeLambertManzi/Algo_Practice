import sys
from collections import Counter

finput = sys.stdin.readline
fprint = sys.stdout.write

# l'exo ne passe pas en python, exo trop vieux qui n'a pas prevu le coup
def main():
    # recup entrees
    lignes, colonnes = map(int, finput().split())
    tab_origine = [list(map(int, finput().split())) for _ in range(lignes)]
    tab_target = [list(map(int, finput().split())) for _ in range(lignes)]

    # creation d'une liste regroupant tous les 1 de tab_origine
    tab_origine_redux = list()
    for i in range(lignes):
        for j in range(colonnes):
            if tab_origine[i][j]:
                tab_origine_redux.append([i, j])

    # creation d'une liste regroupant tous les 1 de tab_target
    tab_target_redux = list()
    for i in range(lignes):
        for j in range(colonnes):
            if tab_target[i][j]:
                tab_target_redux.append([i, j])

    # recup toutes les translations possibles entre points valant 1
    liste_translas = list()
    for pos1 in tab_origine_redux:
        for pos2 in tab_target_redux:
            liste_translas.append((pos2[0] - pos1[0], pos2[1] - pos1[1]))

    # recup la translation la plus presente et print du max d'occurrences
    counter = Counter(liste_translas).most_common(1)
    max_transla = counter[0][0]
    print(counter[0][1])

    # on applique le vecteur de translation le plus present a tous les points 1 de la premiere liste
    # si correspondance dans liste 2 on valide ce point et on print ces coordonnees
    for pos in tab_origine_redux:
        x_transla = pos[0] + max_transla[0]
        y_transla = pos[1] + max_transla[1]
        if x_transla >= 0 and x_transla < lignes and y_transla >= 0 and y_transla < colonnes:
            if tab_target[x_transla][y_transla]:
                fprint("{} {}".format(x_transla + 1, y_transla + 1) + "\n")


main()

"""
import sys
finput = sys.stdin.readline
fprint = sys.stdout.write
import sys
sys.setrecursionlimit(1000)

"""
