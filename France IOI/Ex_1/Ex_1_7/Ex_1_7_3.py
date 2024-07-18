num_mois = int(input())

if num_mois == 11:
    print(29)
elif num_mois == 4 or num_mois == 5 or num_mois == 6 or num_mois == 10:
    print(31)
else:
    print(30)
