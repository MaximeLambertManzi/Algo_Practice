hauteur = int(input())
nb_folioles = int(input())

if hauteur >= 12 and nb_folioles <= 7:
    print("Dorthonion")
elif hauteur >= 10 and nb_folioles >= 10:
    print("Calaelen")
elif hauteur <= 8 and nb_folioles <= 5:
    print("Falarion")
elif hauteur <= 5 and nb_folioles >= 8:
    print("Tinuviel")
