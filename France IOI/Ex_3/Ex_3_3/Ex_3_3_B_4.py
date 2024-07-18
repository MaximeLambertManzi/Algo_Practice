def is_valide(variable):
    valide = False
    variable_maj = variable.upper()

    if (variable[0] >= "A" and variable[0] <= "Z") or (variable[0] >= "a" and variable[0] <= "z") or variable[0] == "_":
        valide = True
    else:
        return False

    for loop in range(1, len(variable)):
        if (
            (variable[loop] >= "A" and variable[loop] <= "Z")
            or (variable[loop] >= "a" and variable[loop] <= "z")
            or variable[loop] == "_"
            or variable[loop].isdigit()
        ):
            valide = True
        else:
            return False

    return valide


def main():
    nb_noms = int(input())

    for loop in range(nb_noms):
        variable = input()

        if is_valide(variable):
            print("YES")
        else:
            print("NO")


main()

"""
import sys
finput = sys.stdin.readline
fprint = sys.stdout.write

def main():

main()

import sys
sys.setrecursionlimit(1000)

"""
