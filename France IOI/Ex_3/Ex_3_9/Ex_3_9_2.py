def main():

    mot = input()
    len_mot = len(mot)

    max_palin = 1

    for loop in range(1, len_mot - 1):
        gauche = loop - 1
        droite = loop + 1
        taille_palin = 1
        while gauche >= 0 and droite < len_mot and mot[gauche] == mot[droite]:
            gauche -= 1
            droite += 1
            taille_palin += 2
        if taille_palin > max_palin:
            max_palin = taille_palin

    for loop in range(0, len_mot - 1):
        gauche = loop
        droite = loop + 1
        taille_palin = 0
        while gauche >= 0 and droite < len_mot and mot[gauche] == mot[droite]:
            gauche -= 1
            droite += 1
            taille_palin += 2
        if taille_palin > max_palin:
            max_palin = taille_palin

    print(max_palin)


main()


"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
