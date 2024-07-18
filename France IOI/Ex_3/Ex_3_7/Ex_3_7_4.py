def main():
    nb_deplacement = int(input())

    deplacements_raw = input()
    deplacements = []

    cheminement = 0

    for loop in range(len(deplacements_raw)):
        if deplacements_raw[loop] != " ":
            deplacements.append(deplacements_raw[loop])

    for loop in range(len(deplacements)):
        if deplacements[loop] == "(":
            cheminement += 1
        elif deplacements[loop] == ")":
            cheminement -= 1

        if cheminement < 0:
            return print(0)

    if cheminement == 0:
        print(1)
    else:
        print(0)


main()
"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
