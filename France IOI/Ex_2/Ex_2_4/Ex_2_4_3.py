longueur_dentelle = int(input())


def couture(motif, longueur):
    for loop in range(longueur):
        print(motif, end="")
    print()


couture("X", longueur_dentelle)
couture("#", longueur_dentelle)
couture("i", longueur_dentelle)
