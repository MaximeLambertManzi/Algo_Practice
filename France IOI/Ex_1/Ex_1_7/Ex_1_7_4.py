date_debut_soldat_1 = int(input())
date_fin_soldat_1 = int(input())
date_debut_soldat_2 = int(input())
date_fin_soldat_2 = int(input())

amitie_validee = False

for loop in range(date_debut_soldat_1, date_fin_soldat_1 + 1):
    if loop >= date_debut_soldat_2 and loop <= date_fin_soldat_2:
        amitie_validee = True

if amitie_validee:
    print("Amis")
else:
    print("Pas amis")
