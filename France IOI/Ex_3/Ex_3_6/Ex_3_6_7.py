def main():
    nb_matieres = int(input())

    liste_matieres = [input() for _ in range(nb_matieres)]

    liste_matieres.sort()

    for matiere in liste_matieres:
        print(matiere)


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
