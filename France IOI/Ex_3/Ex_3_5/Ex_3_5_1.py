def main():
    nb_lignes, nb_colonnes = map(int, input().split(" "))
    nb_rect = int(input())

    tab = [["." for x in range(nb_colonnes)] for y in range(nb_lignes)]

    for loop in range(nb_rect):
        x_min, y_min, x_max, y_max, couleur = input().split(" ")
        x_min = int(x_min)
        y_min = int(y_min)
        x_max = int(x_max)
        y_max = int(y_max)

        for loop2 in range(x_min, x_max + 1):
            for loop3 in range(y_min, y_max + 1):
                tab[loop2][loop3] = couleur

    for loop1 in range(nb_lignes):
        for loop2 in range(nb_colonnes):
            print(tab[loop1][loop2], end="")
        print()


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
