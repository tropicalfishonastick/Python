import random

# Create a list containing numbers and letters for the lottery
lottery_ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 numbers or letters from the list
winning_combination = random.sample(lottery_ticket, 4)

# Print a message for the winning combination
print(f"Winning combination: {winning_combination}")
