def cle_decalage(loop):
    if loop % 2 == 0:
        return 3 * loop
    else:
        return -5 * loop


def dechiffre(code, decalage):

    code_liste = list(code)

    for loop in range(len(code_liste)):
        if code_liste[loop] >= "a" and code_liste[loop] <= "z":
            code_liste[loop] = chr(((ord(code_liste[loop]) - decalage - ord("a")) % 26) + ord("a"))
        elif code_liste[loop] >= "A" and code_liste[loop] <= "Z":
            code_liste[loop] = chr(((ord(code_liste[loop]) - decalage - ord("A")) % 26) + ord("A"))

    return "".join(code_liste)


def main():
    nb_pages = int(input())

    for loop in range(2, nb_pages + 1):
        a_dechiffrer = input()
        print(dechiffre(a_dechiffrer, cle_decalage(loop)))


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
