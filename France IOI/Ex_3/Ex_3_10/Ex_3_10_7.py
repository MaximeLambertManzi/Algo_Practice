def base_10_to_2(val):

    val_temp = val
    tab_val_base_2 = []

    if val == 0:
        tab_val_base_2 = [0]

    for i in range(30, -1, -1):
        if val >= 2**i:
            tab_val_base_2.append(val_temp // (2**i))
            if val_temp >= 2**i:
                val_temp -= 2**i

    return tab_val_base_2


def main():

    nb = int(input())

    for i in range(1, nb + 1):
        for j in range(1, nb + 1):
            chiffres_base_2 = base_10_to_2(i * j)
            for chiffre in chiffres_base_2:
                print(chiffre, end="")

            print(" ", end="")

        print()


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
