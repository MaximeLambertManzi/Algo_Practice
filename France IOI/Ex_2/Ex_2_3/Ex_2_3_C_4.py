titre = input()
auteur = input()

voyelles = ["A", "E", "I", "O", "U", "Y"]

for loop in range(len(titre)):
    if not (titre[loop] in voyelles) and titre[loop] != " ":
        print(titre[loop], end="")

print()

for loop in range(len(auteur)):
    if not (auteur[loop] in voyelles) and auteur[loop] != " ":
        print(auteur[loop], end="")
