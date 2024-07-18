def main():

    taille = int(input())
    tab = set()

    tab = set(map(int, input().split()))

    doublon = 0

    for nombre in tab:
        if -nombre in tab:
            doublon += 1

    print(doublon // 2)


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
