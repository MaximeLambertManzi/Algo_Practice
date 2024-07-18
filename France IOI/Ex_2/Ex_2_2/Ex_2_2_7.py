nb_habitants = int(input())
fortune_habitant = [0] * nb_habitants
couperet = 0.0

for loop in range(nb_habitants):
    fortune_habitant[loop] = int(input())

fortune_habitant.sort()

if nb_habitants % 2 == 1:
    couperet = fortune_habitant[nb_habitants // 2]

if nb_habitants % 2 == 0:
    couperet = (fortune_habitant[nb_habitants // 2] + fortune_habitant[nb_habitants // 2 - 1]) / 2

print(couperet)
