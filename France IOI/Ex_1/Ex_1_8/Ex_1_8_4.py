nb_pierres_max = int(input())
nb_pierres = 1
hauteur = 1

while nb_pierres <= nb_pierres_max:
    hauteur += 1
    nb_pierres += hauteur**2

nb_pierres -= hauteur**2
hauteur -= 1

print(hauteur)
print(nb_pierres)
