def main():
    # Get an integer using the get_int function
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            # Attempt to get user input and convert it to an integer
            return int(input("What's x?"))
        except ValueError:
            # If a ValueError exception occurs (conversion failed), use the 'pass' statement
            pass


# Call the main function to start the program
main()

# alternate method
def main():
    # Get an integer using the get_int function with a custom prompt
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            # Attempt to get user input and convert it to an integer using the provided prompt
            return int(input(prompt))
        except ValueError:
            # If a ValueError exception occurs (conversion failed), use the 'pass' statement
            pass


# Call the main function to start the program
main()
