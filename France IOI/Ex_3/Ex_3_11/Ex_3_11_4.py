def main():

    nb_lignes, nb_colonnes, nb_aeration = map(int, input().split())

    cave = [[2] for _ in range(nb_lignes + 2)]

    ligne_de_2 = [2] * (nb_colonnes + 2)

    cave[0].extend(ligne_de_2)
    for i in range(1, nb_lignes + 1):
        cave[i].extend(list(map(int, input().split())))
        cave[i].extend([2, 2])
    cave[nb_lignes + 1].extend(ligne_de_2)

    last_pos = [1, 1]
    next_pos = [1, 1]
    compteur = 1

    while next_pos != [nb_lignes, nb_colonnes]:
        if compteur % (nb_aeration + 1) == 0 and compteur != 0:
            print("{} {}".format(next_pos[0] - 1, next_pos[1] - 1))
            compteur = 0
        compteur += 1

        if cave[next_pos[0] + 1][next_pos[1]] == 0 and [next_pos[0] + 1, next_pos[1]] != last_pos:
            last_pos = next_pos
            next_pos = [next_pos[0] + 1, next_pos[1]]
        elif cave[next_pos[0] - 1][next_pos[1]] == 0 and [next_pos[0] - 1, next_pos[1]] != last_pos:
            last_pos = next_pos
            next_pos = [next_pos[0] - 1, next_pos[1]]
        elif cave[next_pos[0]][next_pos[1] + 1] == 0 and [next_pos[0], next_pos[1] + 1] != last_pos:
            last_pos = next_pos
            next_pos = [next_pos[0], next_pos[1] + 1]
        elif cave[next_pos[0]][next_pos[1] - 1] == 0 and [next_pos[0], next_pos[1] - 1] != last_pos:
            last_pos = next_pos
            next_pos = [next_pos[0], next_pos[1] - 1]

    if compteur % (nb_aeration + 1) == 0 and compteur != 0:
        print("{} {}".format(next_pos[0] - 1, next_pos[1] - 1))


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)



    print(next_pos[0])
    print(next_pos[1] + 1)

    print(cave[next_pos[0]][next_pos[1] + 1])

    print([last_pos[0], last_pos[1] + 1])
    print(last_pos)

"""
