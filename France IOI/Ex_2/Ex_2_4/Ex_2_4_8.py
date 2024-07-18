def ligne(motif, longueur):
    for loop in range(longueur):
        print(motif, end="")


def ligne_vide(motif, longueur):
    for loop in range(longueur):
        if loop == 0 or loop == longueur - 1:
            print(motif, end="")
        else:
            print(" ", end="")


def rectangle(lignes, colonnes):
    for loop in range(lignes):
        if loop == 0 or loop == lignes - 1:
            ligne("#", colonnes)
            print()
        else:
            ligne_vide("#", colonnes)
            print()


def triangle(lignes):
    for loop in range(lignes):
        if loop == 0 or loop == lignes - 1:
            ligne("@", loop + 1)
            print()
        else:
            ligne_vide("@", loop + 1)
            print()


nb_X = int(input())
nb_lignes_rect = int(input())
nb_colonnes_rect = int(input())
nb_lignes_triangle = int(input())

ligne("X", nb_X)
print()
print()
rectangle(nb_lignes_rect, nb_colonnes_rect)
print()
triangle(nb_lignes_triangle)
