nb_jetons = int(input())
x_jeton = 0
y_jeton = 0

for loop in range(nb_jetons):
    x_jeton = int(input())
    y_jeton = int(input())

    if x_jeton >= 90 or x_jeton <= 0 or y_jeton > 70 or y_jeton <= 0:
        print("En dehors de la feuille")
    elif ((x_jeton >= 60 and x_jeton <= 85) or (x_jeton >= 15 and x_jeton <= 45)) and (y_jeton >= 60 and y_jeton <= 70):
        print("Dans une zone rouge")

    elif (
        (x_jeton >= 10 and x_jeton <= 85)
        and (y_jeton >= 10 and y_jeton <= 55)
        and not ((x_jeton >= 25 and x_jeton <= 50) and (y_jeton >= 20 and y_jeton <= 45))
    ):
        print("Dans une zone bleue")
    else:
        print("Dans une zone jaune")
