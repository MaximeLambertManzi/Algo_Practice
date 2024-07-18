def suite(terme):
    while terme != 1:
        if terme % 2 == 0:
            terme //= 2
            print(terme, end=" ")
        else:
            terme = terme * 3 + 1
            print(terme, end=" ")


terme = int(input())
suite(terme)
