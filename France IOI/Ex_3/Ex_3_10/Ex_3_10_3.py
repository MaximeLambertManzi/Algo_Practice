def main():
    nb = input()
    nb_liste = list(nb)
    nb_liste_calc = nb_liste[::-1]

    nb_base_10 = 0

    for i in range(len(nb_liste)):
        nb_base_10 += int(nb_liste_calc[i]) * (2**i)

    print(nb_base_10)


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
