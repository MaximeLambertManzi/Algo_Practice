import sys

finput = sys.stdin.readline
fprint = sys.stdout.write


def main():
    nb_eleves, nb_presents = map(int, input().split(" "))
    tableau_presence = [False for _ in range(nb_presents + 1)]
    index = 0
    total_appel = 0
    for i in range(nb_presents):
        eleve = int(finput())
        if eleve <= nb_presents:
            tableau_presence[eleve - 1] = True
            total_appel += 1
        if total_appel == nb_eleves:
            print(-1)
        else:
            for j in range(index, nb_presents + 1):
                if tableau_presence[j] == False:
                    fprint(str(j + 1) + "\n")
                    index = j
                    break


main()

"""
import sys
finput = sys.stdin.readline
fprint = sys.stdout.write
import sys
sys.setrecursionlimit(1000)

"""
