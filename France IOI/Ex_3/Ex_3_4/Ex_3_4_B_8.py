def maximum_lettre(texte):

    texte_maj = texte.upper()
    texte_maj_liste = list(texte_maj)
    text_len = len(texte_maj_liste)

    alphabet_count = [0] * 26

    for lettre in range(text_len):
        if texte_maj_liste[lettre].isalpha():

            alphabet = ord(texte_maj_liste[lettre]) - ord("A")
            alphabet_count[alphabet] += 1

    max_lettre = alphabet_count.index(max(alphabet_count)) + ord("A")

    return chr(max_lettre).lower()


def decalage(lettre_max):
    cle = ord(lettre_max) - ord("e")

    return cle


def dechiffre(code, decalage):

    code_liste = list(code)

    for loop in range(len(code_liste)):
        if code_liste[loop] >= "a" and code_liste[loop] <= "z":
            code_liste[loop] = chr(((ord(code_liste[loop]) - decalage - ord("a")) % 26) + ord("a"))
        elif code_liste[loop] >= "A" and code_liste[loop] <= "Z":
            code_liste[loop] = chr(((ord(code_liste[loop]) - decalage - ord("A")) % 26) + ord("A"))

    return "".join(code_liste)


def main():
    ligne = input()

    print(dechiffre(ligne, decalage(maximum_lettre(ligne))))


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
