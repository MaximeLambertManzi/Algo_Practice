nb_cubes_base = 17
total_cubes = 0 

for loop in range(9):
    total_cubes += nb_cubes_base**3
    nb_cubes_base -= 2
        
print(total_cubes)
