import sys


def check_if_in(densite, demande, min, max):

    if min == max:
        return demande == densite[min]

    middle = (min + max) // 2

    if demande <= densite[middle]:
        return check_if_in(densite, demande, min, middle)
    else:
        return check_if_in(densite, demande, middle + 1, max)


def main():

    nb_blocs = int(sys.stdin.readline().strip())

    densite_blocs = list(map(int, sys.stdin.readline().strip().split(" ")))
    densite_blocs.sort()

    nb_questions = int(sys.stdin.readline().strip())

    for loop in range(nb_questions):
        demande = int(sys.stdin.readline().strip())

        if check_if_in(densite_blocs, demande, 0, nb_blocs - 1):
            sys.stdout.write("1" + "\n")
        else:
            sys.stdout.write("0" + "\n")


main()


"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
