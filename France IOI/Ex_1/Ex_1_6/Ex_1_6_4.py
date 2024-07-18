nb_montees_descentes = int(input())
montee_descente = 0
total_montees = 0
total_descentes = 0

for loop in range(nb_montees_descentes):
    montee_descente = int(input())

    if montee_descente >= 0:
        total_montees += montee_descente
    else:
        total_descentes += montee_descente

print(total_montees)
print(-total_descentes)
