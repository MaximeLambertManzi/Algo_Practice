def main():

    val_max = int(input())

    for i in range(30):
        if 2**i == val_max:
            return print(val_max)
        elif 2**i > val_max:
            return print(2 ** (i - 1))


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
