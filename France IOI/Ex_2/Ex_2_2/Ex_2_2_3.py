nb_operations = int(input())

stock = [0] * 10

for loop in range(nb_operations):
    indice = int(input()) - 1
    changement = int(input())

    stock[indice] += changement

for loop in range(10):
    print(stock[loop])
