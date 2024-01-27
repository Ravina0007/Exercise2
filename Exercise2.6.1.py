#3-digit code where each number is between 0 and 9.

import random

def generate_combination():
    combination = ""
    for _ in range(3):
        digit = random.randint(0, 9)
        combination += str(digit)
    return combination


combination1 = generate_combination()
combination2 = generate_combination()

print("Combination 1:", combination1)
print("Combination 2:", combination2)