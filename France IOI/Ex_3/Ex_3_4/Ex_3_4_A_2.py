def main():
    nb_livres = int(input())
    liste_livres = [""] * nb_livres
    for loop in range(nb_livres):
        liste_livres[loop] = input()

    liste_livres.sort()

    for loop in range(nb_livres):
        print(liste_livres[loop])


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