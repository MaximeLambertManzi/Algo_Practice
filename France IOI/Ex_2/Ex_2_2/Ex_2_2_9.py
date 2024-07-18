nb_positions = int(input())
nb_changements_positions = int(input())

plan_de_table = [0] * nb_positions

for loop in range(nb_positions):
    plan_de_table[loop] = int(input())

for loop in range(nb_changements_positions):
    pos_1 = int(input())
    pos_2 = int(input())

    plan_de_table[pos_1], plan_de_table[pos_2] = plan_de_table[pos_2], plan_de_table[pos_1]

for loop in range(nb_positions):
    print(plan_de_table[loop])
