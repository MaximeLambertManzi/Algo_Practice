def main():
    nb_operations = int(input())
    pile = []

    for loop in range(nb_operations):
        qte, annee = map(int, input().split())

        if qte >= 0:
            for loop2 in range(qte):
                pile.append(annee)
        else:
            for loop2 in range(-qte):
                del pile[0]

    print(min(pile))


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
