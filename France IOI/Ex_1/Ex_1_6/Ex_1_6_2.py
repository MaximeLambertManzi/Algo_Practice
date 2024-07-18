pos_actuelle = int(input())
nb_village = int(input())

total_proche = 0
village_localisation = 0
distance = 0

for loop in range(nb_village):
    village_localisation = int(input())
    distance = pos_actuelle - village_localisation

    if distance <= 50 and distance >= -50:
        total_proche += 1

print(total_proche)
