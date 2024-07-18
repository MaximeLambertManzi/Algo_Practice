import sys


def close(target, a, b):
    dist1 = 0
    dist2 = 0
    if target - a >= 0:
        dist1 = target - a
    else:
        dist1 = a - target
    if target - b >= 0:
        dist2 = target - b
    else:
        dist2 = b - target
    if dist1 == dist2:
        return min(a, b)
    elif dist1 < dist2:
        return a
    else:
        return b


def check_if_in(densite, demande, min, max, closest):
    if min == max:
        closest = close(demande, closest, densite[min])
        return closest

    middle = (min + max) // 2

    if demande == densite[middle]:
        return demande
    elif demande < densite[middle]:
        closest_temp = close(demande, densite[middle - 1], densite[middle + 1])
        closest = close(demande, closest, closest_temp)
        return check_if_in(densite, demande, min, middle, closest)
    else:
        closest_temp = close(demande, densite[middle - 1], densite[middle + 1])
        closest = close(demande, closest, closest_temp)
        return check_if_in(densite, demande, middle + 1, max, closest)


def main():
    nb_blocs = int(sys.stdin.readline().strip())
    densite_blocs = list(map(int, sys.stdin.readline().strip().split(" ")))
    densite_blocs.sort()

    nb_questions = int(sys.stdin.readline().strip())

    if nb_blocs == 1:
        for loop in range(nb_questions):
            demande = int(sys.stdin.readline())
            print(densite_blocs[0])
    elif nb_blocs == 2:
        for loop in range(nb_questions):
            demande = int(sys.stdin.readline())
            print(close(demande, densite_blocs[0], densite_blocs[1]))
    else:
        for loop in range(nb_questions):
            demande = int(sys.stdin.readline())
            reponse = check_if_in(densite_blocs, demande, 0, nb_blocs - 1, densite_blocs[1])
            sys.stdout.write("{}".format(reponse) + "\n")


main()

"""
import sys
finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
