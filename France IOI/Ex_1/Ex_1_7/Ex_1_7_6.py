nb_paires = int(input())

for loop in range(nb_paires):
    x_min_1 = int(input())
    x_max_1 = int(input())
    y_min_1 = int(input())
    y_max_1 = int(input())

    x_min_2 = int(input())
    x_max_2 = int(input())
    y_min_2 = int(input())
    y_max_2 = int(input())

    if x_max_1 <= x_min_2 or x_min_1 >= x_max_2 or y_max_1 >= y_min_2 or y_min_1 >= y_max_2:
        print("NON")
    else:
        print("OUI")
