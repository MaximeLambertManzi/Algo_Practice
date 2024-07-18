nb_maison = int(input())
x_maison = 0
y_maison = 0

x_min = 1000000
x_max = 0
y_min = 1000000
y_max = 0

perimetre = 0

for loop in range(nb_maison):
    x_maison = int(input())
    y_maison = int(input())

    if x_maison > x_max:
        x_max = x_maison
    if x_maison < x_min:
        x_min = x_maison

    if y_maison > y_max:
        y_max = y_maison
    if y_maison < y_min:
        y_min = y_maison

perimetre = ((x_max - x_min) + (y_max - y_min)) * 2

print(perimetre)
