nb_emplacements = int(input())

emplacements = [0] * nb_emplacements
marchands = [0] * nb_emplacements

for loop in range(nb_emplacements):
    emplacements[loop] = int(input())

for loop in range(nb_emplacements):
    marchands[emplacements[loop]] = loop

for loop in range(nb_emplacements):
    print(marchands[loop])
