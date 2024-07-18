morceau = [] * 500
morceau = list(input())

doublon = True

while doublon:

    len_morceau = len(morceau)

    for loop in range(len_morceau - 1):
        if morceau[loop] == morceau[loop + 1]:
            morceau[loop] = 0
            morceau[loop + 1] = 0

    doublon = False

    for loop in range(len_morceau):
        if morceau[loop] == 0:
            doublon = True

    if doublon:
        for loop in range(len_morceau - 1, 0, -1):
            if morceau[loop] == 0:
                morceau.remove(morceau[loop])

    if len_morceau == 1 and morceau[0] == 0:
        doublon = False

if len_morceau == 1 and morceau[0] == 0:
    print("")
else:
    print("".join(morceau))
