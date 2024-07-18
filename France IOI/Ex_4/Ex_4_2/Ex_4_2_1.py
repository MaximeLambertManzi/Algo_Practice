def main():

    nb_total = int(input())
    tab = list(map(int, input().split()))

    nb_a_check = int(input())
    tab_a_check = list(map(int, input().split()))

    solution = list()

    for i in range(nb_a_check):
        val = tab_a_check[i]
        solution.append(val)
        while val != 0:
            val = tab[val - 1]
            if val != 0:
                solution.append(val)

        for i in range(len(solution) - 1, -1, -1):
            print(solution[i], end=" ")
        print()

        solution.clear()


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
