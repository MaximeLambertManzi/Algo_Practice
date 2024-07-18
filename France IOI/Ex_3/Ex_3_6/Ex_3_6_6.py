def main():

    nb_bacs = int(input())

    bacs = [[0] * 2 for loop in range(nb_bacs)]

    for loop in range(nb_bacs):
        bacs[loop] = list(map(int, input().split(" ")))

    bacs.sort(key=lambda x: (x[1], x[0]))

    for loop in range(nb_bacs):
        print("{} {}".format(bacs[loop][0], bacs[loop][1]))


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
