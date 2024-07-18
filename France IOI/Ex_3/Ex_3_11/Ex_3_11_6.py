def main():

    nb_cables = int(input())
    cables = [[0, 0, 0] for _ in range(nb_cables)]

    pile_1 = []
    pile_2 = []
    pile_3 = []

    min_same_output_1 = 0
    min_same_output_2 = 0
    total_taille = 0

    for i in range(nb_cables):
        entree, sortie, taille = map(int, input().split())
        cables[i] = [entree, sortie, taille]

    cables.sort(key=lambda x: x[2], reverse=True)

    for i in range(nb_cables):
        if cables[i][0] == 1 and cables[i][1] == 1:
            pile_1.append(cables[i])
        elif cables[i][0] == 0 and cables[i][1] == 0:
            pile_2.append(cables[i])
        else:
            pile_3.append(cables[i])

    taille_1 = len(pile_1)
    taille_2 = len(pile_2)
    taille_3 = len(pile_3)

    if taille_1 == 0:
        return print(-1)
    elif taille_2 == 0:
        min_same_output_1 = 1
        min_same_output_2 = 0
    elif taille_1 > taille_2:
        min_same_output_2 = min(taille_1, taille_2)
        min_same_output_1 = min_same_output_2 + 1
    else:
        min_same_output_2 = min(taille_1, taille_2)
        min_same_output_1 = min_same_output_2
        min_same_output_2 -= 1

    for i in range(min_same_output_1):
        total_taille += pile_1[i][2]
    for i in range(min_same_output_2):
        total_taille += pile_2[i][2]
    for i in range(taille_3):
        total_taille += pile_3[i][2]

    print(total_taille)


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
