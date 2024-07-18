de_1 = int(input())
de_2 = int(input())
somme = de_1 + de_2
taxe = 0

if somme >= 10:
    taxe = 36
    print("Taxe spéciale !")
    print(taxe)
else:
    taxe = somme * 2
    print("Taxe régulière")
    print(taxe)