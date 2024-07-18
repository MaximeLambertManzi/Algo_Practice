def main():

    longueur_centrale, longueur_riviere = map(int, input().split())
    puissance_courants = list(map(int, input().split(" ")))

    max_puissance = 0
    max_temp = 0

    for loop in range(longueur_centrale):
        max_puissance += puissance_courants[loop]

    max_temp = max_puissance

    for loop in range(longueur_centrale, longueur_riviere):

        max_temp += puissance_courants[loop] - puissance_courants[loop - longueur_centrale]

        if max_temp > max_puissance:
            max_puissance = max_temp

    print(max_puissance)


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
