from sys import stdin


def main():

    total = 0
    lines = stdin.read().splitlines()

    for loop in range(len(lines)):
        inner_line = lines[loop].split(" ")
        for loop in range(len(inner_line)):
            total += int(inner_line[loop])

    print(total)


main()


"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

def main():

main()

import sys
sys.setrecursionlimit(1000)

try:
   entier = int(input())
except:
   # On a pas réussi à lire l'entier
   print("Une erreur est arrivée")

"""
