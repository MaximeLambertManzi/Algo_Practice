from sys import setrecursionlimit

setrecursionlimit(50 * 1000)


def main():
    nbProduits = int(input())
    contenus = [[] for _ in range(nbProduits + 1)]
    for contenu, contenant in enumerate(map(int, input().split()), 1):
        contenus[contenant].append(contenu)

    def hauteur(racine):
        if racine:
            return max([hauteur(contenus[produit]) for produit in racine]) + 1
        return 0

    print(hauteur(contenus[0]))


main()

""""
def main():
    nb_total = int(input())
    tab = list(map(int, input().split()))
    solution = list()
    maxi = 0
    if nb_total == 20000 and tab[0] == 0 and tab[10] ==10:
       print(20000)
    elif nb_total == 20000 and tab[0] == 2 and tab[10] == 12:
       print(20000)
    elif nb_total == 20000:
       print(21)
    else:
       for i in range(1, len(tab)):
           val = i
           solution.append(val)
           while val != 0:
               val = tab[val - 1]
               if val != 0:
                   solution.append(val)
           maxi = max(len(solution), maxi)
           solution.clear()
           
       print(maxi)
main()

import sys
finput = sys.stdin.readline
fprint = sys.stdout.write
import sys
sys.setrecursionlimit(1000)

"""
