import sys

finput = sys.stdin.readline
fprint = sys.stdout.write


def main():

    auteur = finput()
    age_fils = int(finput())

    print(ord(auteur[0]) - 64, end="")
    print(chr(age_fils + 64))


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
