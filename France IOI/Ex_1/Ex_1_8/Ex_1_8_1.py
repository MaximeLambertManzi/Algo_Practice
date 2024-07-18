pop_totale = int(input())
nb_malades = 1
jour = 1

while nb_malades < pop_totale:
    nb_malades *= 3
    jour += 1

print(jour)
