def main():

    texte = input()
    texte_maj = texte.upper()
    texte_maj_liste = list(texte_maj)
    text_len = len(texte_maj_liste)

    alphabet_count = [0] * 26

    for lettre in range(text_len):
        if texte_maj_liste[lettre] != " ":

            alphabet = ord(texte_maj_liste[lettre]) - ord("A")
            alphabet_count[alphabet] += 1

    max_lettre = alphabet_count.index(max(alphabet_count)) + ord("A")
    print(chr(max_lettre))


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
