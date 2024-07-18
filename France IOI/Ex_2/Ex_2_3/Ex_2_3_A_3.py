nb_lignes = int(input())
texte = [0] * nb_lignes

for loop in range(nb_lignes):
    texte[loop] = input()

for loop in range(nb_lignes):
    if loop % 2 == 0:
        print(texte[loop])
