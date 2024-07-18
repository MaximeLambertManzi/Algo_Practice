lettre_cible = input()
nb_lignes = int(input())

nb_lettre_cible = 0

for loop in range(nb_lignes):
    texte = input()
    for loop in range(len(texte)):
        if texte[loop] == lettre_cible:
            nb_lettre_cible += 1

print(nb_lettre_cible)
