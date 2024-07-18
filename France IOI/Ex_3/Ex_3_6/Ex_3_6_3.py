import sys


def main():
    nb_voitures = int(input())

    demarrage = list(map(int, sys.stdin.readline().strip().split()))

    liste_depassement1 = [0 for _ in range((nb_voitures**2) // 2)]
    liste_depassement2 = [0 for _ in range((nb_voitures**2) // 2)]

    arrivee = [loop + 1 for loop in range(nb_voitures)]

    nb_depassement = 0
    loop0 = 0

    while demarrage != arrivee:
        for loop in range(nb_voitures - 1, 0, -1):

            if demarrage[loop] == loop0 + 1 and demarrage[loop] != loop + 1:
                demarrage[loop - 1], demarrage[loop] = demarrage[loop], demarrage[loop - 1]

                liste_depassement1[nb_depassement] = demarrage[loop]
                liste_depassement2[nb_depassement] = demarrage[loop - 1]

                nb_depassement += 1

        loop0 += 1

    print(nb_depassement)

    for i in range(nb_depassement):
        print("{} {}".format(liste_depassement1[i], liste_depassement2[i]))


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
