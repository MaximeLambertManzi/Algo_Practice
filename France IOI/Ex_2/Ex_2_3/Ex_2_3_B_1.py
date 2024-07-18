nb_personnes = int(input())

for loop in range(nb_personnes):
    nom = input().split(" ")
    print("{} {}".format(nom[1], nom[0]))
