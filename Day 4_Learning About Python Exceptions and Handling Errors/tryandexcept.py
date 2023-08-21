try:
    # Attempt to get user input and convert it to an integer
    x = int(input("What's x?"))
    
    # If conversion is successful, print the value of x
    print(f"x is {x}")
    
except ValueError:
    # If a ValueError exception occurs (conversion failed), print an error message
    print("x is not an integer")

# alternate method
try:
    # Attempt to get user input and convert it to an integer
    x = int(input("What's x?"))
except ValueError:
    # If a ValueError exception occurs (conversion failed), print an error message
    print("x is not an integer")

# Print the value of x (whether it's an integer or not)
print(f"x is {x}")
