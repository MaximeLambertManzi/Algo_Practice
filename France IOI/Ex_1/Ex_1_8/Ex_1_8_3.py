valeur = int(input())
essai = 0
nb_essais = 0

while essai != valeur:
    nb_essais += 1
    essai = int(input())

    if essai < valeur:
        print("c'est plus")
    elif essai > valeur:
        print("c'est moins")

print("Nombre d'essais nécessaires :")
print(nb_essais)
