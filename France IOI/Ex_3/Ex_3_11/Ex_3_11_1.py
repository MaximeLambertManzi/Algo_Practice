def main():
    nb_a = int(input())
    liste_a = list(map(int, input().split()))

    nb_b = int(input())
    liste_b = list(map(int, input().split()))

    for i in range(len(liste_b)):
        liste_a.append(liste_b[i])

    liste_a.sort()

    for i in range(len(liste_a)):
        print(liste_a[i], end=" ")


main()
"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
