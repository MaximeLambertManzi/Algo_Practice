jeu_1 = input()
jeu_2 = input()

nb_egalite = 0
loop = 0
winner = 0
sortie = 0

nb_cartes_1 = len(jeu_1)
nb_cartes_2 = len(jeu_2)

while sortie < 100:

    if jeu_1[loop] == jeu_2[loop]:
        nb_egalite += 1

    if jeu_1[loop] > jeu_2[loop]:
        winner = 2
        sortie = 100
    elif jeu_1[loop] < jeu_2[loop]:
        winner = 1
        sortie = 100
    elif loop + 2 > nb_cartes_1 and loop + 2 > nb_cartes_2:
        winner = "="
        sortie = 100
    elif loop + 2 > nb_cartes_1:
        winner = 2
        sortie = 100
    elif loop + 2 > nb_cartes_2:
        winner = 1
        sortie = 100
    else:
        winner = "="

    loop += 1

print(winner)
print(nb_egalite)
