def main():
    nb_bacs_stocks, nb_bacs_camion = map(int, input().split(" "))

    bacs_stocks = [0] * nb_bacs_stocks
    bacs_stocks = list(map(int, input().split(" ")))

    bacs_stocks.sort(reverse=True)

    for loop in range(nb_bacs_camion):
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
