from math import *

taxe_fruits = float(input())
new_taxe_fruits = float(input())
prix_actuel = float(input())
new_prix = 0.0

prix_hors_taxe = prix_actuel / ((100 + taxe_fruits) / 100)
new_prix = prix_hors_taxe + new_taxe_fruits / 100 * prix_hors_taxe

new_prix = round(new_prix * 100) / 100

print(new_prix)
