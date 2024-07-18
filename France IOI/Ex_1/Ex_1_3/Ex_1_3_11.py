"""

from robot import *

num_anneau = 1

for loop in range(10):
    for loop in range(num_anneau):
        droite()
        
    ramasser()

    for loop in range(num_anneau):
        gauche()

    deposer()
    
    num_anneau += 1
    
"""