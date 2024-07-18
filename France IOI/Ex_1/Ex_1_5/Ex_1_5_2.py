num_borne_1 = int(input())
num_borne_2 = int(input())
distance = 0

if num_borne_1 >= num_borne_2:
    distance = num_borne_1 - num_borne_2
else:
    distance = num_borne_2 - num_borne_1
    
print(distance)