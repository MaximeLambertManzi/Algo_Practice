texte = input()
caracteres = list(texte)

for loop in range(len(caracteres)):
    if caracteres[loop] == " ":
        caracteres[loop] = "_"

texte = "".join(caracteres)
print(texte)

""" V2 avec split

texte = input().split(" ")
texte = "_".join(texte)

print(texte)

"""
