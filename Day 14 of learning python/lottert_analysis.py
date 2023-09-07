import random

# Create a list containing numbers and letters for the lottery
lottery_ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define your own ticket (you can change this)
my_ticket = [1, 2, 'A', 'B']

attempts = 0
while True:
    # Randomly select 4 numbers or letters from the list
    winning_combination = random.sample(lottery_ticket, 4)
    attempts += 1

    # Check if your ticket matches the winning combination
    if my_ticket == winning_combination:
        print(f"Congratulations! You won after {attempts} attempts.")
        break
