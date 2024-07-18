nb_lignes = int(input())
nb_colonnes = int(input())
motif = input()


def remplissage(nb_lignes, nb_colonnes, motif):
    for loop in range(nb_lignes):
        for loop in range(nb_colonnes):
            print(motif, end="")
        print()


remplissage(nb_lignes, nb_colonnes, motif)
