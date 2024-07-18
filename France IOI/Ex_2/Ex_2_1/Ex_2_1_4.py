nb_notes = int(input())
note = 0
somme_notes = 0
moyenne = 0.0

for loop in range(nb_notes):
    note = int(input())
    somme_notes += note

moyenne = somme_notes / nb_notes

print(moyenne)
