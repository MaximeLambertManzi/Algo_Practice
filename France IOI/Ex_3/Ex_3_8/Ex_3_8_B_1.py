def completor(start, finish):
    if start == finish:
        print(finish)
        return
    else:
        print(start, end=" ")
        completor(start + 1, finish)


def main():

    start, finish = map(int, input().split())

    completor(start, finish)


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
