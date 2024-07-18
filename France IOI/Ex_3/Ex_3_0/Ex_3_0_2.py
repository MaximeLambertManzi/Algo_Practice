nb_lettres = int(input())
target_size = nb_lettres * 2 - 1

if target_size % 2 == 0:
    middle = target_size // 2
else:
    middle = target_size // 2 + 1

for loop in range(target_size):
    ligne = loop + 1
    val_init = ord("a") - 1

    if ligne <= middle:

        for loop in range(target_size):
            if loop < ligne:
                val_init += 1
                print(chr(val_init), end="")

            elif loop >= ((nb_lettres * 2) - ligne):
                val_init -= 1
                print(chr(val_init), end="")

            else:
                print(chr(val_init), end="")

    if ligne > middle:
        ligne2 = target_size - loop

        for loop in range(target_size):
            if loop < ligne2:
                val_init += 1
                print(chr(val_init), end="")

            elif loop >= ((nb_lettres * 2) - ligne2):
                val_init -= 1
                print(chr(val_init), end="")

            else:
                print(chr(val_init), end="")

    print()
