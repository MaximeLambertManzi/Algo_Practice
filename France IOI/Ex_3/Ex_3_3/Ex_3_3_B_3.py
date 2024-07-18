def is_palindrome(livre):
    is_palindrome = True

    livre_maj = livre.upper()
    livre_travail = "".join(livre_maj.split(" "))

    for lettre in range(len(livre_travail)):
        if livre_travail[lettre] != livre_travail[len(livre_travail) - lettre - 1]:
            is_palindrome = False

    return is_palindrome


def main():
    nb_livres = int(input())

    for loop in range(nb_livres):
        livre = input()

        if is_palindrome(livre):
            print(livre)


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
