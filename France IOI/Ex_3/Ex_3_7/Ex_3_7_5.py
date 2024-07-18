def check_if_duplicate(liste):
    for item in liste:
        if liste.count(item) > 1:
            return item
    return -1


def check_if_duplicate_2(listOfElems):
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return elem
        else:
            setOfElems.add(elem)
    return -1


def main():
    nb_clients = int(input())

    liste_clients = list(map(int, input().split(" ")))

    print(check_if_duplicate_2(liste_clients))


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
