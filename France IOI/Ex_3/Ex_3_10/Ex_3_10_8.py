def mean(liste):
    sum = 0
    for i in range(len(liste)):
        sum += liste[i]
    return sum // len(liste)


def base_16_redux(nb_origine_liste):
    for loop in range(len(nb_origine_liste)):
        if nb_origine_liste[loop] == "A":
            nb_origine_liste[loop] = 10
        elif nb_origine_liste[loop] == "B":
            nb_origine_liste[loop] = 11
        elif nb_origine_liste[loop] == "C":
            nb_origine_liste[loop] = 12
        elif nb_origine_liste[loop] == "D":
            nb_origine_liste[loop] = 13
        elif nb_origine_liste[loop] == "E":
            nb_origine_liste[loop] = 14
        elif nb_origine_liste[loop] == "F":
            nb_origine_liste[loop] = 15
        else:
            nb_origine_liste[loop] = int(nb_origine_liste[loop])

    return nb_origine_liste


def base_16_redux_reverse(nb_origine_liste):
    for loop in range(len(nb_origine_liste)):
        if nb_origine_liste[loop] == 10:
            nb_origine_liste[loop] = "A"
        elif nb_origine_liste[loop] == 11:
            nb_origine_liste[loop] = "B"
        elif nb_origine_liste[loop] == 12:
            nb_origine_liste[loop] = "C"
        elif nb_origine_liste[loop] == 13:
            nb_origine_liste[loop] = "D"
        elif nb_origine_liste[loop] == 14:
            nb_origine_liste[loop] = "E"
        elif nb_origine_liste[loop] == 15:
            nb_origine_liste[loop] = "F"
        else:
            nb_origine_liste[loop] = int(nb_origine_liste[loop])

    return nb_origine_liste


def base_16_to_10(chiffres):

    nombre_decimal = 0

    for chiffre in chiffres:
        nombre_decimal = (nombre_decimal * 16) + chiffre
    return nombre_decimal


def base_10_to_16(nombre):
    chiffres = []
    encoreUnChiffre = True
    while encoreUnChiffre:
        chiffres = chiffres + [nombre % 16]
        nombre = nombre // 16
        encoreUnChiffre = nombre > 0

    return chiffres[::-1]


def main():
    nb_16 = input()
    nb_redux = base_16_redux(list(nb_16))
    nb_10 = base_16_to_10(nb_redux)

    total = [0] * nb_10

    for loop in range(nb_10):
        nb_16_temp = input()
        nb_redux_temp = base_16_redux(list(nb_16_temp))
        nb_10_temp = base_16_to_10(nb_redux_temp)

        total[loop] = nb_10_temp

    liste_total = base_16_redux_reverse(base_10_to_16(mean(total)))

    for chiffre in liste_total:
        print(chiffre, end="")


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
