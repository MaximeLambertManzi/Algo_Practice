def main():
    mot_target = input().upper()
    ligne = input().upper().split(" ")
    total_target = 0

    for loop in range(len(ligne)):
        if ligne[loop] == mot_target:
            total_target += 1

    print(total_target)


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
