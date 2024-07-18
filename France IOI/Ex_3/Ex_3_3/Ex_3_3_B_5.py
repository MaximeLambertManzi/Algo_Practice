def nb_lettre(texte):

    texte_maj = texte.upper()
    texte_maj_liste = list(texte_maj)
    text_len = len(texte_maj_liste)

    alphabet_count = [0] * 26

    for lettre in range(text_len):
        if texte_maj_liste[lettre] >= "A" and texte_maj_liste[lettre] <= "Z":

            alphabet = ord(texte_maj_liste[lettre]) - ord("A")
            alphabet_count[alphabet] += 1

    return alphabet_count


def total_lettre(count):
    total = 0
    for loop in range(len(count)):
        total += count[loop]

    return total


def proba_lettre(count, total):
    proba = 0.0
    for loop in range(len(count)):
        proba = count[loop] / total
        print(proba)


def main():

    texte = input()
    alphabet_count = nb_lettre(texte)
    total_alphabet = total_lettre(alphabet_count)

    proba_lettre(alphabet_count, total_alphabet)


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
