def hanoi(nb_disque, pos1, pos2, pos3):
    if nb_disque == 1:
        print("{} -> {}".format(pos1, pos2))
    else:
        hanoi(nb_disque - 1, pos1, pos3, pos2)
        print("{} -> {}".format(pos1, pos2))
        hanoi(nb_disque - 1, pos3, pos2, pos1)


def main():

    nb = int(input())
    hanoi(nb, 1, 3, 2)


main()


"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
