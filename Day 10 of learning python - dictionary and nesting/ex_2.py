'''Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.'''

# Create a dictionary to store people's favorite numbers
favorite_numbers = {
    'Alice': 42,
    'Bob': 7,
    'Charlie': 14,
    'David': 27,
    'Eve': 8
}

# Print each person's name and their favorite number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
