nb_lignes = int(input())


for loop in range(nb_lignes):
    ligne = input()
    len_ligne = len(ligne)
    for loop in range(len_ligne):
        print(ligne[len_ligne - loop - 1], end="")
    print()
