nb_charrettes = int(input())

charrettes_poids = [0.0] * nb_charrettes

total_poids = 0.0
moyenne_poids = 0.0

for loop in range(nb_charrettes):
    charrettes_poids[loop] = float(input())
    total_poids += charrettes_poids[loop]

moyenne_poids = total_poids / nb_charrettes

for loop in range(nb_charrettes):
    print(-(charrettes_poids[loop] - moyenne_poids))
