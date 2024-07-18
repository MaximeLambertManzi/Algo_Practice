def main():
    nb_bacs_stocks, nb_bacs_insert = map(int, input().split(" "))

    bacs_stocks = [0] * nb_bacs_stocks

    try:
        bacs_stocks = list(map(int, input().split(" ")))
    except:
        bacs_stocks = []

    bacs_insert = [0] * nb_bacs_insert
    bacs_insert = list(map(int, input().split(" ")))

    indice_stocks = [0] * nb_bacs_insert

    bacs_stocks.sort()

    for loop in range(nb_bacs_insert):
        for loop2 in range(nb_bacs_stocks + loop):
            if bacs_insert[loop] > bacs_stocks[loop2]:
                indice_stocks[loop] = loop2 + 1

        bacs_stocks.append(bacs_insert[loop])
        bacs_stocks.sort()

    for loop in range(nb_bacs_insert):
        print(indice_stocks[loop], end=" ")

    print()

    for loop in range(nb_bacs_stocks + nb_bacs_insert):
        print(bacs_stocks[loop], end=" ")


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
