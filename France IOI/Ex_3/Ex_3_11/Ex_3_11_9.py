def main():

    taille_dico = int(input())
    dico = [input() for _ in range(taille_dico)]
    dico_temp = list()
    dico_final = list()

    taille_mot = int(input())

    lettre = input()
    for k in range(taille_dico):
        for j in range(4):
            if len(dico[k]) >= 1:
                if lettre[j] == dico[k][0]:
                    dico_final.append(dico[k])

    for i in range(1, taille_mot):
        lettre = input()
        for k in range(len(dico_final)):
            for j in range(4):
                if len(dico_final[k]) == taille_mot:
                    if lettre[j] == dico_final[k][i]:
                        dico_temp.append(dico_final[k])

        dico_final = dico_temp.copy()
        dico_temp.clear()

    print(dico_final[0])


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
