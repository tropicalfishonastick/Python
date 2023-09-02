'''Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready.'''

# Ask the user how many people are in their dinner group
group_size = input("How many people are in your dinner group? ")
group_size = int(group_size)  # Convert the input to an integer

# Check if the group size is more than eight and print an appropriate message
if group_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")
