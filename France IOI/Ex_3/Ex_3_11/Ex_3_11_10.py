def print_tab(plateau, lignes, colonnes):
    for i in range(lignes):
        for j in range(colonnes):
            print(plateau[i][j], end="")
        print()


def main():
    lignes, colonnes = map(int, input().split())

    plateau = [list(input()) for __ in range(lignes)]

    nb_operations = int(input())
    operations = input()

    for x in range(nb_operations):

        if operations[x] == "S":
            for i in range(lignes - 1, 0, -1):
                for j in range(1, colonnes - 1):
                    if plateau[i][j] == "x":
                        k = i + 1
                        while plateau[k][j] == ".":
                            k += 1
                        if plateau[k][j] == "O":
                            plateau[i][j] = "."
                        else:
                            plateau[i][j] = "."
                            plateau[k - 1][j] = "x"

        elif operations[x] == "N":
            for i in range(1, lignes - 1):
                for j in range(1, colonnes - 1):
                    if plateau[i][j] == "x":
                        k = i - 1
                        while plateau[k][j] == ".":
                            k -= 1
                        if plateau[k][j] == "O":
                            plateau[i][j] = "."
                        else:
                            plateau[i][j] = "."
                            plateau[k + 1][j] = "x"

        elif operations[x] == "E":
            for i in range(1, lignes - 1):
                for j in range(colonnes - 1, 0, -1):
                    if plateau[i][j] == "x":
                        k = j + 1
                        while plateau[i][k] == ".":
                            k += 1
                        if plateau[i][k] == "O":
                            plateau[i][j] = "."
                        else:
                            plateau[i][j] = "."
                            plateau[i][k - 1] = "x"

        elif operations[x] == "O":
            for i in range(1, lignes - 1):
                for j in range(1, colonnes - 1):
                    if plateau[i][j] == "x":
                        k = j - 1
                        while plateau[i][k] == ".":
                            k -= 1
                        if plateau[i][k] == "O":
                            plateau[i][j] = "."
                        else:
                            plateau[i][j] = "."
                            plateau[i][k + 1] = "x"

    total = 0
    for i in range(lignes):
        for j in range(colonnes):
            if plateau[i][j] == "x":
                total += 1

    print(total)


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
