import sys


def main():

    nb_bacs = int(input())

    valeur_bacs = list(map(int, sys.stdin.readline().split()))

    valeur_bacs.sort()

    for loop in range(nb_bacs):
        print(valeur_bacs[loop], end=" ")


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
