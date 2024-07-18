def crochetage(nb, crochets):
    print("[", end="")
    if crochets == 1:
        print(nb, end="")
    else:
        crochetage(nb, crochets - 1)
    print("]", end="")


def main():
    nb, crochets = map(int, input().split(" "))

    if crochets >= 1:
        crochetage(nb, crochets)
    else:
        print(nb)


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
