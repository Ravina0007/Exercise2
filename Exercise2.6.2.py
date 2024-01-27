# 4-digit code where each number is between 1 and 6.

import random

def generate_combination():
    combination = ""
    for _ in range(4):
        digit = random.randint(1, 6)
        combination += str(digit)
    return combination

combination1 = generate_combination()
combination2 = generate_combination()


print("Combination 1:", combination1)
print("Combination 2:", combination2)