from curses.ascii import islower


def main():

    plateau = [["."] * 12 for _ in range(12)]
    pieces = [] * 8
    pieces_ligne = ["."] * 2
    ending_ligne = [".", "."]

    for loop in range(8):
        pieces = list(input())
        pieces_ligne.extend(pieces)
        pieces_ligne.extend(ending_ligne)

        plateau[loop + 2] = pieces_ligne

        pieces_ligne = ["."] * 2

    for x in range(12):
        for y in range(12):
            if plateau[x][y] == "C":
                if plateau[x - 2][y + 1].islower():
                    return print("yes")
                if plateau[x - 2][y - 1].islower():
                    return print("yes")
                if plateau[x - 1][y + 2].islower():
                    return print("yes")
                if plateau[x - 1][y - 2].islower():
                    return print("yes")
                if plateau[x + 1][y + 2].islower():
                    return print("yes")
                if plateau[x + 1][y - 2].islower():
                    return print("yes")
                if plateau[x + 2][y + 1].islower():
                    return print("yes")
                if plateau[x + 2][y - 1].islower():
                    return print("yes")

    return print("no")


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
