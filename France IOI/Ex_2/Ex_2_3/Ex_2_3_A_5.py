nb_livres = int(input())

max_titre = 0

for loop in range(nb_livres):
    titre = input()
    len_titre = len(titre)
    if len_titre > max_titre:
        print(titre)
        max_titre = len_titre
