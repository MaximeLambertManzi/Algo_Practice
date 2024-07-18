def base_X_to_10(chiffres, base_source):

    nombre_decimal = 0

    for chiffre in chiffres:
        nombre_decimal = (nombre_decimal * base_source) + chiffre
    return list(str(nombre_decimal))


def base_10_to_X(val, base):

    val_temp = val

    liste_chiffre = [0] * 30
    compteur_chiffre = 0

    if val == 0:
        return print("0")

    for i in range(30, -1, -1):
        if val >= base**i:
            chiffre = val_temp // (base**i)
            liste_chiffre[i] = chiffre
            compteur_chiffre += 1
            if val_temp >= base**i:
                val_temp -= chiffre * (base**i)

    for chffre in liste_chiffre[compteur_chiffre - 1 :: -1]:
        print(chffre, end=" ")


def main():

    base_origine, base_target, taille_origine = map(int, input().split(" "))
    nb_origine = list(map(int, input().split(" ")))

    nb_base_10 = base_X_to_10(nb_origine, base_origine)
    nb_base_target = base_10_to_X(int("".join(nb_base_10)), base_target)


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
