def mid(pos1, pos2):
    pos_mid = [0, 0]

    if pos1[0] - pos2[0] > 0:
        pos_mid[0] = (pos1[0] + pos2[0]) // 2 + 1
    else:
        pos_mid[0] = (pos2[0] + pos1[0]) // 2

    if pos1[1] - pos2[1] > 0:
        pos_mid[1] = (pos1[1] + pos2[1]) // 2 + 1
    else:
        pos_mid[1] = (pos2[1] + pos1[1]) // 2

    return pos_mid


def sierpinski(dessin, pos1, pos2, pos3, taille):
    if taille > 1:

        dessin[pos1[0]][pos1[1]] = "#"
        dessin[pos2[0]][pos2[1]] = "#"
        dessin[pos3[0]][pos3[1]] = "#"

        sierpinski(dessin, pos1, mid(pos1, pos2), mid(pos1, pos3), taille // 2)
        sierpinski(dessin, mid(pos2, pos1), pos2, mid(pos2, pos3), taille // 2)
        sierpinski(dessin, mid(pos3, pos1), mid(pos3, pos2), pos3, taille // 2)


def main():

    taille = int(input())
    dessin = [[" "] * taille for _ in range(taille)]

    pos1 = [0, 0]
    pos2 = [0, taille - 1]
    pos3 = [taille - 1, 0]

    sierpinski(dessin, pos1, pos2, pos3, taille)

    if taille == 1:
        print("#")

    else:

        for loop1 in range(taille):
            for loop2 in range(taille):
                print(dessin[loop1][loop2], end="")
            print()


main()


"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
