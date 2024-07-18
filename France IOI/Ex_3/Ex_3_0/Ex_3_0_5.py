nb_grenouille = int(input())
nb_tour = int(input())

distance_grenouille = [0] * nb_grenouille
nb_tour_devant = [0] * nb_grenouille


def max_strict(liste):
    nb_max = 0
    max_value = max(liste)
    for loop in range(0, len(liste)):
        if liste[loop] == max_value:
            nb_max += 1

    if nb_max > 1:
        return -1

    else:
        return max_value
    # si 2 sont en tete ils doivent recup zero point


for loop in range(nb_tour):

    if loop < nb_tour - 1:
        num, distance = map(int, input().split(" "))
        distance_grenouille[num - 1] += distance

        max_distance_grenouille = max_strict(distance_grenouille)
        if max_distance_grenouille != -1:

            max_distance_grenouille_index = distance_grenouille.index(max_distance_grenouille)
            nb_tour_devant[max_distance_grenouille_index] += 1

max_distance_grenouille_final = max(nb_tour_devant)
max_distance_grenouille_index_final = nb_tour_devant.index(max_distance_grenouille_final)

print(max_distance_grenouille_index_final + 1)
