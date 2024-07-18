def is_acronyme(titre, acronyme):
    titre_test = titre.upper()
    titre_test_split = titre_test.split(" ")
    acro_test = ""

    for loop in range(len(titre_test_split)):
        acro_test += titre_test_split[loop][0]

    if acro_test == acronyme:
        return True
    else:
        return False


def affichage_propre(titre):
    titre = titre.lower()
    titre_split = titre.split(" ")
    new_titre = ""

    for loop in range(len(titre_split)):
        new_titre += titre_split[loop][0].upper() + titre_split[loop][1:] + " "

    print(new_titre)


def main():
    init_acronyme = input()
    nb_livres = int(input())

    for loop in range(nb_livres):
        titre = input()

        if is_acronyme(titre, init_acronyme):
            affichage_propre(titre)


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
