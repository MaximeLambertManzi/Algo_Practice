def main():
    nb_mots = int(input())

    dictionnaire = [""] * nb_mots

    for loop in range(nb_mots):
        mot1, mot2 = input().split(" ")
        dictionnaire[loop] = mot2 + " " + mot1

    dictionnaire.sort()

    for loop in range(nb_mots):
        print(dictionnaire[loop])


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
