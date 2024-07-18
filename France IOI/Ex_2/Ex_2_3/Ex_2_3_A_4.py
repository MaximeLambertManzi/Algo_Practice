nb_livres = int(input())
longueur_min = int(input())

for loop in range(nb_livres):
    titre = input()
    resume = input()

    if len(resume) < longueur_min:
        print(titre)
