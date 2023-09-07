'''Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers'''

# Create a dictionary to store favorite numbers for different people
favorite_numbers = {
    'Alice': [42, 7, 11],
    'Bob': [3, 8],
    'Carol': [13, 5, 9]
}

# Loop through the dictionary and print each person's name and their favorite numbers
for person, numbers in favorite_numbers.items():
    print(f"{person}'s Favorite Numbers:")
    for number in numbers:
        print(f"- {number}")
    print("\n")
