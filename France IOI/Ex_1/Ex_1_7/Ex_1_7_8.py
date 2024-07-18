date_debut = int(input())
date_fin = int(input())

nb_invites = int(input())
arrivee = 0
depart = 0

suspect = False
nb_suspect = 0

for loop in range(nb_invites):
    arrivee = int(input())
    depart = int(input())

    if arrivee > date_fin or depart < date_debut:
        suspect = False
    else:
        suspect = True

    if suspect:
        nb_suspect += 1

print(nb_suspect)
