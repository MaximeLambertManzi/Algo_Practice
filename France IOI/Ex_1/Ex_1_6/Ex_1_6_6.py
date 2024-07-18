age = int(input())
poids_bagages = int(input())

prix = 0

if age == 60:
    prix = 0
elif age < 10:
    prix = 5
else:
    if poids_bagages >= 20:
        prix = 40
    else:
        prix = 30

print(prix)
