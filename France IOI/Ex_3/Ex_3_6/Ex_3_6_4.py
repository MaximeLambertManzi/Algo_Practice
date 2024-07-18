import sys


def main():

    nb_bacs = int(input())

    pollution_bacs = list(map(int, sys.stdin.readline().strip().split()))

    pollution_bacs.sort()

    for loop in range(nb_bacs):
        print(pollution_bacs[loop], end=" ")


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
