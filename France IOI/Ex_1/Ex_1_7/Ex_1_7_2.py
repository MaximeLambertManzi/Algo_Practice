x_min = int(input())
x_max = int(input())
y_min = int(input())
y_max = int(input())

nb_maison = int(input())
total_maison_suspectes = 0

for loop in range(nb_maison):
    x_maison = int(input())
    y_maison = int(input())

    if x_maison >= x_min and x_maison <= x_max and y_maison >= y_min and y_maison <= y_max:
        total_maison_suspectes += 1

print(total_maison_suspectes)
