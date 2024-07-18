prix_kg_ingredients = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]

poids = 0
cout_total = 0

for loop in range(10):
    poids = int(input())
    cout_total += poids * prix_kg_ingredients[loop]

print(cout_total)
