'''Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do
each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.'''

# Using conditional test in the while statement
while input("Enter 'quit' to exit: ") != 'quit':
    pass

# Using an active variable to control the loop
active = True
while active:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        active = False

# Using a break statement to exit the loop
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
