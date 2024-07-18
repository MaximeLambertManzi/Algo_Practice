nb_lignes, nb_mots = map(int, input().split(" "))

nb_lettres = [0] * 101
phrase = [0] * nb_mots

for loop in range(nb_lignes):
    phrase = input().split(" ")

    for loop in range(nb_mots):
        nb_lettres[len(phrase[loop])] += 1

for loop in range(101):
    if nb_lettres[loop] != 0:
        print("{} : {}".format(loop, nb_lettres[loop]))
