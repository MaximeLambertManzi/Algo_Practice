def demand_code(code_entree):
    code = 0
    while code != code_entree:
        print("Entrez le code :")
        code = int(input())


demand_code(4242)
print("Premier code bon.")
demand_code(2121)
print("Bravo.")
