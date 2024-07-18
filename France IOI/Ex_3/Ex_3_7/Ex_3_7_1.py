def main():
    nb_types = int(input())
    qte_produits = list(map(int, input().split(" ")))
    nb_operations = int(input())

    type = 0
    qte = 0

    for loop in range(nb_operations):
        type, qte = map(int, input().split(" "))

        qte_produits[type - 1] += qte

    for qte_final in qte_produits:
        print(qte_final, end=" ")


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
