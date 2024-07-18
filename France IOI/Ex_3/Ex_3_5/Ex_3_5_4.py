def horz_win(plateau, taille, joueur):
    cumul_sum = 0

    for x in range(taille):
        for y in range(taille):

            if plateau[x][y] == joueur:
                cumul_sum += 1
                if cumul_sum == 5:
                    return 100
            else:
                cumul_sum = 0

        cumul_sum = 0

    return cumul_sum


def vert_win(plateau, taille, joueur):
    cumul_sum = 0

    for x in range(taille):
        for y in range(taille):

            if plateau[y][x] == joueur:
                cumul_sum += 1
                if cumul_sum == 5:
                    return 100
            else:
                cumul_sum = 0

        cumul_sum = 0

    return cumul_sum


def diag_win(plateau, taille, joueur):
    cumul_sum = 0

    for x in range(taille):
        for y in range(taille):
            for z in range(taille):
                if x + z < taille and y + z < taille:
                    if plateau[x + z][y + z] == joueur:
                        cumul_sum += 1
                        if cumul_sum == 5:
                            return 100
                    else:
                        cumul_sum = 0
            cumul_sum = 0

    cumul_sum = 0

    for x in range(taille):
        for y in range(taille):
            for z in range(taille):
                if x + z < taille and y + z >= 0:
                    if plateau[x + z][y - z] == joueur:
                        cumul_sum += 1
                        if cumul_sum == 5:
                            return 100
                    else:
                        cumul_sum = 0

    return cumul_sum


def main():
    taille = int(input())
    plateau = [[0] * taille for _ in range(taille)]

    for loop in range(taille):
        plateau[loop] = list(map(int, input().split(" ")))

    if (
        vert_win(plateau, taille, 1) == 100
        or horz_win(plateau, taille, 1) == 100
        or diag_win(plateau, taille, 1) == 100
    ):
        print("1")
    elif (
        vert_win(plateau, taille, 2) == 100
        or horz_win(plateau, taille, 2) == 100
        or diag_win(plateau, taille, 2) == 100
    ):
        print("2")
    else:
        print("0")


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
