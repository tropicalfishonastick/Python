# Import the 'random' module to access random number generation functions
import random

# Use the 'random.choice()' function to select a random item from the provided list
# In this case, the list contains two options: "heads" and "tails"
coin = random.choice(["heads", "tails"])

# Print the result of the coin toss, which could be either "heads" or "tails"
print(coin)

# improving above code:
# Import the 'choice' function from the 'random' module to directly access random item selection
from random import choice

# Use the 'choice()' function to randomly select an item from the provided list
# The list contains two options: "heads" and "tails"
coin = choice(["heads", "tails"])

# Print the result of the coin toss, which could be either "heads" or "tails"
print(coin)


# consider the function random.randint(a, b). This function will generate a random number between a and b. Modify your code as follows:
# Import the 'random' module to generate random numbers and values
import random

# Use the 'randint()' function from the 'random' module to generate a random integer between 1 and 10 (inclusive)
number = random.randint(1, 10)

# Print the randomly generated number
print(number)


# We can introduce into our card random.shuffle(x) where it will shuffle a list into a random order.
# Import the 'random' module to work with randomization
import random

# A list of playing cards
cards = ["jack", "queen", "king"]

# Shuffle the order of cards using the 'shuffle()' function from the 'random' module
random.shuffle(cards)

# Iterate through each card in the shuffled list and print them
for card in cards:
    print(card)

