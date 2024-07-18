def main():

    val = int(input())
    val_temp = val

    if val == 0:
        print("0")

    for i in range(30, -1, -1):
        if val >= 2**i:
            print(val_temp // (2**i), end="")
            if val_temp >= 2**i:
                val_temp -= 2**i


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
