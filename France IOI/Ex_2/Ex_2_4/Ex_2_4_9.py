def convertisseur(valeur, unite):
    if unite == "m":
        valeur /= 0.3048
        print("{} p".format(valeur))
    elif unite == "g":
        valeur *= 0.002205
        print("{} l".format(valeur))
    elif unite == "c":
        valeur = valeur * 1.8 + 32
        print("{} f".format(valeur))


nb_valeurs = int(input())

for loop in range(nb_valeurs):
    valeur, unite = input().split(" ")
    valeur = float(valeur)
    convertisseur(valeur, unite)
