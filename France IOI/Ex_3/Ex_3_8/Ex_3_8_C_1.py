def reverse_recurr(texte, taille):
    if taille == 0:
        return
    else:
        print(texte[taille - 1], end="")
        reverse_recurr(texte, taille - 1)


def main():

    texte = input()
    taille = len(texte)

    reverse_recurr(texte, taille)


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
