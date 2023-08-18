# Prompt the user for input and store it as a string named 'name'
name = input("What's your name? ")

# Check if the entered name matches specific names
if name == "Harry":
    # If the name is "Harry", print the house "Gryffindor"
    print("Gryffindor")
elif name == "Hermione":
    # If the name is "Hermione", print the house "Gryffindor"
    print("Gryffindor")
elif name == "Ron": 
    # If the name is "Ron", print the house "Gryffindor"
    print("Gryffindor")
elif name == "Draco":
    # If the name is "Draco", print the house "Slytherin"
    print("Slytherin")
else:
    # If the name is none of the above, print "Who?"
    print("Who?")


# alternate way of solving above program
# Prompt the user for input and store it as a string named 'name'
name = input("What's your name? ")

# Check if the entered name matches specific names for Gryffindor
if name == "Harry" or name == "Hermione" or name == "Ron": 
    # If the name is "Harry", "Hermione", or "Ron", print the house "Gryffindor"
    print("Gryffindor")
# Check if the entered name is "Draco" for Slytherin
elif name == "Draco":
    # If the name is "Draco", print the house "Slytherin"
    print("Slytherin")
# If the name is none of the above, print "Who?"
else:
    print("Who?")


# another way of solving above program
# Prompt the user for input and store it as a string named 'name'
name = input("What's your name? ")

# Using the new match statement to determine the house based on the entered name
match name:
    # Check if the entered name matches any of the names for Gryffindor
    case "Harry":
        # If the name is "Harry", print the house "Gryffindor"
        print("Gryffindor")
    case "Hermione":
        # If the name is "Hermione", print the house "Gryffindor"
        print("Gryffindor")
    case "Ron":
        # If the name is "Ron", print the house "Gryffindor"
        print("Gryffindor")
    case "Draco":
        # If the name is "Draco", print the house "Slytherin"
        print("Slytherin")
    case _:
        # If the name is none of the above, print "Who?"
        print("Who?")


# another way of solving above program
# Prompt the user for input and store it as a string named 'name'
name = input("What's your name? ")

# Using the new match statement to determine the house based on the entered name
match name:
    # Check if the entered name matches any of the names for Gryffindor using the "|" (or) operator
    case "Harry" | "Hermione" | "Ron":
        # If the name is "Harry", "Hermione", or "Ron", print the house "Gryffindor"
        print("Gryffindor")
    case "Draco":
        # If the name is "Draco", print the house "Slytherin"
        print("Slytherin")
    case _:
        # If the name is none of the above, print "Who?"
        print("Who?")
