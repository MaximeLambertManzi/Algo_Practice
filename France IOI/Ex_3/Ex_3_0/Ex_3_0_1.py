nb_livres, nb_jours = map(int, input().split(" "))

livres = [0] * nb_livres

for loop in range(nb_jours):
    nb_clients = int(input())

    for loop in range(nb_clients):
        indice_livre, duree = map(int, input().split(" "))

        if livres[indice_livre] > 0:
            print("0")
        else:
            print("1")
            livres[indice_livre] = duree

    for loop in range(len(livres)):
        livres[loop] -= 1
