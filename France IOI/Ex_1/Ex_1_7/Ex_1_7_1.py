date_debut = int(input())
date_fin = int(input())

nb_entrees = int(input())
entrees = 0

suspects = 0

for loop in range(nb_entrees):
    entrees = int(input())

    if entrees >= date_debut and entrees <= date_fin:
        suspects += 1

print(suspects)
