'''Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.'''

# Ask the user for a number
number = input("Enter a number: ")
number = int(number)  # Convert the input to an integer

# Check if the number is a multiple of 10 and print an appropriate message
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
