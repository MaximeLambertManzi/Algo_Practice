volume_total = 0
largeur_max = int(input())
largeur_min = int(input())

for loop in range(largeur_min, largeur_max+1):
    volume_total += loop**2

print(volume_total)