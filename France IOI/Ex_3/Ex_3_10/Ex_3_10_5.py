def main():

    val, base = map(int, input().split(" "))
    val_temp = val

    liste_chiffre = [0] * 30
    compteur_chiffre = 0

    if val == 0:
        print("1")
        return print("0")

    for i in range(30, -1, -1):
        if val >= base**i:
            chiffre = val_temp // (base**i)
            liste_chiffre[i] = chiffre
            compteur_chiffre += 1
            if val_temp >= base**i:
                val_temp -= chiffre * (base**i)

    print(compteur_chiffre)
    for chffre in liste_chiffre[compteur_chiffre - 1 :: -1]:
        print(chffre, end=" ")


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
