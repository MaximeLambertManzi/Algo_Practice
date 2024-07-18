from math import *

pop_actuelle = int(input())
croissance_previ = float(input())

print(floor(pop_actuelle * (100 + croissance_previ) / 100))
