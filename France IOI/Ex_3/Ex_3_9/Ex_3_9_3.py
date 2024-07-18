def main():
    nb_points = int(input())
    total = 0

    tab = []
    set_tab = set()

    for loop in range(nb_points):
        x_0, y_0 = map(int, input().split())
        tab.append((x_0, y_0))
        set_tab.add((x_0, y_0))

    set_doublon = set()

    for i in range(nb_points):
        for j in range(i + 1, nb_points):

            middle = tuple()
            if (tab[i][0] + tab[j][0]) % 2 == 0 and (tab[i][1] + tab[j][1]) % 2 == 0:
                middle = (((tab[i][0] + tab[j][0]) // 2), (tab[i][1] + tab[j][1]) // 2)

            if middle != ():
                if middle in set_tab and middle not in set_doublon:
                    total += 1
                    set_doublon.add(middle)
    print(total)


main()

"""
import sys
finput = sys.stdin.readline
fprint = sys.stdout.write
import sys
sys.setrecursionlimit(1000)

"""
