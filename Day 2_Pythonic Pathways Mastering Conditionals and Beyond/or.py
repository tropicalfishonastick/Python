# Prompt the user for input and store it as integers x and y
x = int(input("What's x? "))
y = int(input("What's y? "))

# Check if x is either less than y or greater than y
if x < y or x > y:
    # If x is not equal to y, print this message
    print("x is not equal to y")
else:
    # If x is equal to y, print this message
    print("x is equal to y")


# alternate way of solving above program
# Prompt the user for input and store it as integers x and y
x = int(input("What's x? "))
y = int(input("What's y? "))

# Check if x is equal to y
if x == y:
    # If x is equal to y, print this message
    print("x is equal to y")
else:
    # If x is not equal to y, print this message
    print("x is not equal to y")


# another way of solving above program
# Prompt the user for input and store it as integers x and y
x = int(input("What's x? "))
y = int(input("What's y? "))

# Check if x is not equal to y
if x != y:
    # If x is not equal to y, print this message
    print("x is not equal to y")
else:
    # If x is equal to y, print this message
    print("x is equal to y")
