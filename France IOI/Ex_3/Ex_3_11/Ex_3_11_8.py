import sys

finput = sys.stdin.readline


def main():

    id = int(input())
    nb_relations = int(input())

    tab_relations = [[] for _ in range(65000)]

    amis_d_amis = list()

    for i in range(nb_relations):
        amis_1, amis_2 = map(int, finput().split())
        tab_relations[amis_1].append(amis_2)
        tab_relations[amis_2].append(amis_1)

    for amis in tab_relations[id]:
        amis_d_amis.extend(tab_relations[amis])

    amis_d_amis.extend(tab_relations[id])

    set_final = set(amis_d_amis)
    set_1 = set(tab_relations[id])
    set_1.add(id)

    print(len(set_final ^ set_1))


main()

"""
import sys

finput = sys.stdin.readline
fprint = sys.stdout.write

import sys
sys.setrecursionlimit(1000)

"""
