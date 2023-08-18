# Prompt the user for input and store it as an integer named 'x'
x = int(input("What's x? "))

# Check if x is divisible evenly by 2 (i.e., if x is even)
if x % 2 == 0:
    # If x is even, print this message
    print("Even")
else:
    # If x is not even, it must be odd, so print this message
    print("Odd")


# alternate way of solving above program
# Define the main function
def main():
    # Prompt the user for input and store it as an integer named 'x'
    x = int(input("What's x? "))
    
    # Call the is_even function to determine if 'x' is even or odd
    if is_even(x):
        # If 'x' is even, print this message
        print("Even")
    else:
        # If 'x' is not even, print this message (which means it's odd)
        print("Odd")


# Define the is_even function that takes an integer 'n' as a parameter
def is_even(n):
    # Check if 'n' is divisible evenly by 2 (i.e., if 'n' is even)
    if n % 2 == 0:
        # If 'n' is even, return True
        return True
    else:
        # If 'n' is not even, return False
        return False

# Call the main function to start the program
main()


# another way of solving above program
# Define the main function
def main():
    # Prompt the user for input and store it as an integer named 'x'
    x = int(input("What's x? "))
    
    # Call the is_even function to determine if 'x' is even or odd
    if is_even(x):
        # If 'x' is even, print this message
        print("Even")
    else:
        # If 'x' is not even, print this message (which means it's odd)
        print("Odd")


# Define the is_even function that takes an integer 'n' as a parameter
def is_even(n):
    # Return True if 'n' is even (remainder of division by 2 is 0), else return False
    return True if n % 2 == 0 else False

# Call the main function to start the program
main()


# another way of solving above program
# Define the main function
def main():
    # Prompt the user for input and store it as an integer named 'x'
    x = int(input("What's x? "))
    
    # Call the is_even function to determine if 'x' is even or odd
    if is_even(x):
        # If 'x' is even, print this message
        print("Even")
    else:
        # If 'x' is not even, print this message (which means it's odd)
        print("Odd")


# Define the is_even function that takes an integer 'n' as a parameter
def is_even(n):
    # Return True if 'n' is even (remainder of division by 2 is 0), else return False
    return n % 2 == 0

# Call the main function to start the program
main()
