nb_membres = int(input())

poids_equipe_1 = 0
total_equipe_1 = 0
poids_equipe_2 = 0
total_equipe_2 = 0

for loop in range(nb_membres):
    poids_equipe_1 = int(input())
    total_equipe_1 += poids_equipe_1
    
    poids_equipe_2 = int(input())
    total_equipe_2 += poids_equipe_2
    
if total_equipe_1 > total_equipe_2:
    print("L'équipe 1 a un avantage")
    
elif total_equipe_2 > total_equipe_1:
    print("L'équipe 2 a un avantage")
    
print("Poids total pour l'équipe 1 :", total_equipe_1)
print("Poids total pour l'équipe 2 :", total_equipe_2)