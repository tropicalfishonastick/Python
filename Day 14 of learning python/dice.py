from random import randint
print(randint(1, 6))

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

# Create a 6-sided die and roll it 10 times
six_sided_die = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    result = six_sided_die.roll_die()
    print(f"Rolled: {result}")

# Create a 10-sided die and roll it 10 times
ten_sided_die = Die(sides=10)
print("\nRolling a 10-sided die 10 times:")
for _ in range(10):
    result = ten_sided_die.roll_die()
    print(f"Rolled: {result}")

# Create a 20-sided die and roll it 10 times
twenty_sided_die = Die(sides=20)
print("\nRolling a 20-sided die 10 times:")
for _ in range(10):
    result = twenty_sided_die.roll_die()
    print(f"Rolled: {result}")
