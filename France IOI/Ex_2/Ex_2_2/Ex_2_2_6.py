nb_deplacements = int(input())
suite_deplacements = [0] * nb_deplacements

for loop in range(nb_deplacements):
    suite_deplacements[loop] = int(input())

for loop in range(nb_deplacements):
    if suite_deplacements[loop] == 5:
        suite_deplacements[loop] = 4
    elif suite_deplacements[loop] == 4:
        suite_deplacements[loop] = 5
    elif suite_deplacements[loop] == 2:
        suite_deplacements[loop] = 1
    elif suite_deplacements[loop] == 1:
        suite_deplacements[loop] = 2

for loop in range(nb_deplacements - 1, -1, -1):
    print(suite_deplacements[loop])
