personne_recherche = int(input())
taille_liste = int(input())
present = False
num = 0

for loop in range(taille_liste):
    num = int(input())

    if personne_recherche == num:
        present = True

if present:
    print("Sorti de la ville")
else:
    print("Encore dans la ville")
