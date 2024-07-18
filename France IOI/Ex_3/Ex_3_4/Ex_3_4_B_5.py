for loop in range(ord("a"), ord("z") + 1):
    if (
        loop != ord("a")
        and loop != ord("e")
        and loop != ord("i")
        and loop != ord("o")
        and loop != ord("u")
        and loop != ord("y")
    ):
        print(chr(loop) + " ", end="")

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

def main():

main()

import sys
sys.setrecursionlimit(1000)

"""
