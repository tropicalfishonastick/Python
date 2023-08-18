# Prompt the user for input and store it as integers x and y
x = int(input("What's x? "))
y = int(input("What's y? "))

# Check if x is less than y
if x < y:
    # If x is less than y, print this message
    print("x is less than y")

# Check if x is greater than y
if x > y:
    # If x is greater than y, print this message
    print("x is greater than y")

# Check if x is equal to y
if x == y:
    # If x is equal to y, print this message
    print("x is equal to y")


# alternate way of solving above program
# Prompt the user for input and store it as integers x and y
x = int(input("What's x? "))
y = int(input("What's y? "))

# Check if x is less than y
if x < y:
    # If x is less than y, print this message
    print("x is less than y")
# If x is not less than y, check if x is greater than y
elif x > y:
    # If x is greater than y, print this message
    print("x is greater than y")
# If neither x is less than y nor x is greater than y, check if x is equal to y
elif x == y:
    # If x is equal to y, print this message
    print("x is equal to y")


# another way of solving above program
# Prompt the user for input and store it as integers x and y
x = int(input("What's x? "))
y = int(input("What's y? "))

# Check if x is less than y
if x < y:
    # If x is less than y, print this message
    print("x is less than y")
# If x is not less than y, check if x is greater than y
elif x > y:
    # If x is greater than y, print this message
    print("x is greater than y")
# If neither x is less than y nor x is greater than y, it means x is equal to y
else:
    # Print this message
    print("x is equal to y")
