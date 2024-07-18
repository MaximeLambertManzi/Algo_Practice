def main():
    nb_a = int(input())
    liste_a = list(map(int, input().split()))
    set_a = set(liste_a)

    nb_b = int(input())
    liste_b = list(map(int, input().split()))
    set_b = set(liste_b)

    total = 0

    if nb_a <= nb_b:
        for i in range(nb_a):
            if liste_a[i] in set_b:
                total += 1

    else:
        for i in range(nb_b):
            if liste_b[i] in set_a:
                total += 1

    print(total)


main()
"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
