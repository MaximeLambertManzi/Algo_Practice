def main():
    base, nb_chiffres = list(map(int, input().split(" ")))

    nb_liste = list(map(int, input().split(" ")))
    nb_liste_calc = nb_liste[::-1]

    nb_base_X = 0

    for i in range(len(nb_liste)):
        nb_base_X += nb_liste_calc[i] * (base**i)

    print(nb_base_X)


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
