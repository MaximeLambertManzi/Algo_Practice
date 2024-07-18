nb_personnes = int(input())

entree_sortie = 0

total_simultane = 0
max_simultane = 0

for loop in range(nb_personnes * 2):
    entree_sortie = int(input())

    if entree_sortie > 0:
        total_simultane += 1
    elif entree_sortie < 0:
        total_simultane -= 1

    if total_simultane > max_simultane:
        max_simultane = total_simultane

print(max_simultane)
