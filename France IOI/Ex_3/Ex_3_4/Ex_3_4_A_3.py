def main():
    nb_livres = int(input())
    liste_livres = [""] * nb_livres

    for loop in range(nb_livres):
        liste_livres[loop] = input()

    liste_a_lire = [""] * nb_livres
    min_alpha = liste_livres[0]

    for loop in range(nb_livres):

        if liste_livres[loop] >= min_alpha:
            liste_a_lire[loop] = liste_livres[loop]
            min_alpha = liste_livres[loop]

    for loop in range(nb_livres):
        if liste_a_lire[loop] != "":
            print(liste_a_lire[loop])


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
