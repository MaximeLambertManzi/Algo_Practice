import sys

finput = sys.stdin.readline
fprint = sys.stdout.write


def main():

    nb_requetes = int(input())

    question = False
    collage = False
    taille = -1
    index_last = 0
    tab = [0] * nb_requetes

    for i in range(nb_requetes):
        entree = finput().strip()
        if entree == "Q":
            question = True
        else:
            collage = True
            temp, taille = entree.split(" ")

        tab[index_last] = int(taille)

        if question:
            fprint(str(index_last) + "\n")

        if collage:
            while index_last != 0 and tab[index_last] >= tab[index_last - 1]:
                tab[index_last - 1] = tab[index_last]
                index_last -= 1

            index_last += 1

        question = False
        collage = False
        taille = -1


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
