def nb_amour(nom):
    nom_value = list(nom)
    love_value_total = 0

    for lettre in nom_value:
        love_value = ord(lettre) - 65
        love_value_total += love_value

    while love_value_total >= 10:
        temp = [int(x) for x in str(love_value_total)]
        love_value_total = sum(temp)

    return love_value_total


def main():
    nom1, nom2 = input().split(" ")

    print(nb_amour(nom1), end=" ")
    print(nb_amour(nom2))


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
