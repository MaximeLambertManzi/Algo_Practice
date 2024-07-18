import sys

finput = sys.stdin.readline
fprint = sys.stdout.write


def main():

    nb_lettres = int(input())

    mot = input()
    tab_affichage = [["."] * ((nb_lettres * 2) - 1) for _ in range((nb_lettres * 2) - 1)]

    delay = 0

    for k in range(nb_lettres):
        for i in range(delay, (nb_lettres * 2) - 1 - delay):
            for j in range(delay, (nb_lettres * 2) - 1 - delay):
                tab_affichage[i][j] = mot[nb_lettres - delay - 1]
        delay += 1

    for i in range((nb_lettres * 2) - 1):
        for j in range((nb_lettres * 2) - 1):
            fprint(tab_affichage[i][j])
        fprint("\n")


main()


"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
