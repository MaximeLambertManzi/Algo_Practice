def min2(ent1, ent2):
    if ent1 <= ent2:
        return ent1
    else:
        return ent2


val1 = int(input())
val2 = int(input())
min = min2(val1, val2)

for loop in range(8):
    val1 = int(input())

    min = min2(val1, min)

print(min)
