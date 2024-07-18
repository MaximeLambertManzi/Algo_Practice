total_nb_mesures = int(input())
temp_min = int(input())
temp_max = int(input())

temperature = int(input())

while total_nb_mesures > 1 and temperature >= temp_min and temperature <= temp_max:
    print("Rien à signaler")
    total_nb_mesures -= 1
    temperature = int(input())

if temperature >= temp_min and temperature <= temp_max:
    print("Rien à signaler")

if not (temperature >= temp_min and temperature <= temp_max):
    print("Alerte !!")
