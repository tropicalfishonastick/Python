try:
    # Attempt to get user input and convert it to an integer
    x = int(input("What's x?"))
except ValueError:
    # If a ValueError exception occurs (conversion failed), print an error message
    print("x is not an integer")
else:
    # If no exception occurred, print the value of x
    print(f"x is {x}")


# alternate method
while True:
    try:
        # Attempt to get user input and convert it to an integer
        x = int(input("What's x?"))
    except ValueError:
        # If a ValueError exception occurs (conversion failed), print an error message
        print("x is not an integer")
    else:
        # If no exception occurred, break out of the loop
        break

# Print the value of x (successfully converted integer)
print(f"x is {x}")

# alternate method : creating function to get an integer
def main():
    # Get an integer using the get_int function
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            # Attempt to get user input and convert it to an integer
            x = int(input("What's x?"))
        except ValueError:
            # If a ValueError exception occurs (conversion failed), print an error message
            print("x is not an integer")
        else:
            # If no exception occurred, break out of the loop
            break
    return x


# Call the main function to start the program
main()

#alternate method
def main():
    # Get an integer using the get_int function
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            # Attempt to get user input and convert it to an integer
            x = int(input("What's x?"))
        except ValueError:
            # If a ValueError exception occurs (conversion failed), print an error message
            print("x is not an integer")
        else:
            # If no exception occurred, return the obtained integer and exit the loop
            return x


# Call the main function to start the program
main()

#alternate method
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
            # If a ValueError exception occurs (conversion failed), print an error message
            print("x is not an integer")


# Call the main function to start the program
main()
