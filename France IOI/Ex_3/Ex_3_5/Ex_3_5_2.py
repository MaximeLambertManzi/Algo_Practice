def check_validite(carre, taille):
    liste_nb = [0] * (taille**2)

    for loop1 in range(taille):
        for loop2 in range(taille):
            if (carre[loop1][loop2] > taille**2) or (carre[loop1][loop2] <= 0):
                return False

            liste_nb[carre[loop1][loop2] - 1] += 1

            if liste_nb[carre[loop1][loop2] - 1] > 1:
                return False

    return True


def check_lignes(carre, taille):
    total = sum(carre[0])
    sum_lignes = 0

    for x in range(taille):
        for y in range(taille):
            sum_lignes += carre[x][y]

        if sum_lignes != total:
            return False, total

        sum_lignes = 0

    return True, total


def check_colonnes(carre, taille, nb_magique):
    sum_colonnes = 0

    for x in range(taille):
        for y in range(taille):
            sum_colonnes += carre[y][x]

        if sum_colonnes != nb_magique:
            return False

        sum_colonnes = 0

    return True


def check_diags(carre, taille, nb_magique):
    sum_diags = 0

    for loop in range(taille):
        sum_diags += carre[loop][loop]

    if sum_diags != nb_magique:
        return False

    sum_diags = 0

    for loop in range(taille):
        sum_diags += carre[taille - loop - 1][loop]

    if sum_diags != nb_magique:
        return False

    return True


def main():
    taille = int(input())
    carre = [[0] * taille for _ in range(taille)]

    for loop in range(taille):
        carre[loop] = list(map(int, input().split(" ")))

    valid = check_validite(carre, taille)
    nb_magique = 0

    if not valid:
        return print("no")

    valid, nb_magique = check_lignes(carre, taille)

    if not valid:
        return print("no")

    valid = check_colonnes(carre, taille, nb_magique)

    if not valid:
        return print("no")

    valid = check_diags(carre, taille, nb_magique)

    if not valid:
        return print("no")
    else:
        return print("yes")


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
