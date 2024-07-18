def toto(nb):
    if nb == 0:
        return

    print("(", end="")
    toto(nb - 1)

    if nb == 1:
        print("0", end="")

    print(" + ", end="")

    if nb == 1:
        print("0", end="")

    toto(nb - 1)
    print(")", end="")


def main():
    nb = int(input())

    print("0 = ", end="")
    if nb == 0:
        print("0")
    else:
        toto(nb)


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
