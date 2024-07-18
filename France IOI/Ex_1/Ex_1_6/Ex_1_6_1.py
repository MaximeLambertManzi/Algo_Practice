nb_lieux = int(input())
nb_bigcity = 0
taille_city = 0

for loop in range(nb_lieux):
    taille_city = int(input())
    if taille_city > 10000:
        nb_bigcity += 1

print(nb_bigcity)
