nb_produits = int(input())
nb_personnes = int(input())

pref = 0
produits_like = [0] * nb_produits

for loop in range(nb_personnes):
    pref = int(input())
    produits_like[pref] += 1

for loop in range(nb_produits):
    print(produits_like[loop])
