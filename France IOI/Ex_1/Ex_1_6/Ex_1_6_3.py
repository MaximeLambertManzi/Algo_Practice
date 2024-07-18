nb_jours_marche = int(input())
distance = 0
record = 0

for loop in range(nb_jours_marche):
    distance = int(input())

    if distance > record:
        record = distance

print(record)
