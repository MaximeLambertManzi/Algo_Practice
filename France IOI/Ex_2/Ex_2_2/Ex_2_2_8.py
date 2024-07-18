nb_participant = int(input())

num_participant = [0] * nb_participant

for loop in range(nb_participant):
    num_participant[loop] = int(input())

num_participant.sort()
nb_pair = nb_participant // 2

for loop in range(nb_pair):
    print("{} {}".format(num_participant[loop], num_participant[nb_participant - 1 - loop]))
