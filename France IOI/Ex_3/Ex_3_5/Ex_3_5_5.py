def check_erase(motif, x, y):
    if motif[x - 1][y] != "#":
        return False
    if motif[x + 1][y] != "#":
        return False
    if motif[x][y + 1] != "#":
        return False
    if motif[x][y - 1] != "#":
        return False

    return True


def main():
    nb_iterations = int(input())
    hauteur, largeur = map(int, input().split(" "))

    motif = [list(input()) for _ in range(hauteur)]
    motif2 = [["."] * largeur for _ in range(hauteur)]

    for loop in range(nb_iterations):

        for x in range(1, hauteur - 1):
            for y in range(1, largeur - 1):
                if check_erase(motif, x, y):
                    motif2[x][y] = motif[x][y]

        if loop != (nb_iterations - 1):
            motif = motif2
            motif2 = [["."] * largeur for _ in range(hauteur)]

    for loop1 in range(hauteur):
        for loop2 in range(largeur):
            print(motif2[loop1][loop2], end="")
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
