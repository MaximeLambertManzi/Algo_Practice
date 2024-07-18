def lisser(liste):
    len_liste = len(liste)

    liste_lisse = [0.0] * len_liste

    for loop in range(len_liste):
        if loop == 0 or loop == len_liste - 1:
            liste_lisse[loop] = liste[loop]
        else:
            liste_lisse[loop] = (liste[loop - 1] + liste[loop + 1]) / 2

    return liste_lisse


def val_absolue(valeur):
    if valeur < 0:
        return -valeur
    else:
        return valeur


def check_distance(liste, distance):
    len_liste = len(liste)
    lissage_ok = True

    for loop in range(len_liste - 1):
        if val_absolue(liste[loop] - liste[loop + 1]) >= distance:
            lissage_ok = False

    return lissage_ok


nb_mesures = int(input())
diff_max = float(input())
liste = [0.0] * nb_mesures
nb_iterations = 0

for loop in range(nb_mesures):
    liste[loop] = float(input())

lissage_ok = check_distance(liste, diff_max)

while not (lissage_ok):
    liste = lisser(liste)
    nb_iterations += 1
    lissage_ok = check_distance(liste, diff_max)


print(nb_iterations)
