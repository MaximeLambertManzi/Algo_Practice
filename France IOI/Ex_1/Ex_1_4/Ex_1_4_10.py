nb_karvas = int(input())
note_karvas = 0 

for loop in range(nb_karvas):
    poids = int(input())
    age = int(input())
    longueur_cornes = int(input())
    hauteur = int(input())
    
    note_karvas = longueur_cornes * hauteur + poids
    
    print(note_karvas)