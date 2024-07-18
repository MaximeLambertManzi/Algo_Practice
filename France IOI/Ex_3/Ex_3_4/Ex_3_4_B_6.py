def dechiffre(code, grille):
    grille_maj = grille.upper()

    sortie_liste = list(code)

    for loop in range(len(sortie_liste)):
        if sortie_liste[loop] >= "a" and sortie_liste[loop] <= "z":
            sortie_liste[loop] = grille[ord(sortie_liste[loop]) - ord("a")]
        elif sortie_liste[loop] >= "A" and sortie_liste[loop] <= "Z":
            sortie_liste[loop] = grille_maj[ord(sortie_liste[loop]) - ord("A")]

    return "".join(sortie_liste)


def main():
    grille_dechiffrage = input()
    a_dechiffrer = input()

    print(dechiffre(a_dechiffrer, grille_dechiffrage))


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

def main():

main()

import sys
sys.setrecursionlimit(1000)

"""
