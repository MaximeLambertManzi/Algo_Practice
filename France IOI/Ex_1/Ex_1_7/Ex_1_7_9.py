nb_personnes = int(input())
note = 0

for loop in range(nb_personnes):
    taille = int(input())
    age = int(input())
    poids = int(input())
    cheval = int(input())
    bruns = int(input())

    if taille >= 178 and taille <= 182:
        note += 1
    if age >= 34:
        note += 1
    if poids < 70:
        note += 1
    if cheval == 0:
        note += 1
    if bruns == 1:
        note += 1

    if note == 5:
        print("Très probable")
    elif note == 3 or note == 4:
        print("Probable")
    elif note == 0:
        print("Impossible")
    else:
        print("Peu probable")

    note = 0
