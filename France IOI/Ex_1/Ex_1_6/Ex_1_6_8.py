nb_marchands = int(input())
prix_galetttes = 0
prix_min = 1000000
best_position = 0
position = 1

for loop in range(nb_marchands):
    prix_galetttes = int(input())

    if prix_galetttes <= prix_min:
        prix_min = prix_galetttes
        best_position = position

    position += 1

print(best_position)
