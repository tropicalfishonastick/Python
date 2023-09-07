'''Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made. 

No Pastrami: Using the list sandwich_orders, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches'''

# Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.
sandwich_orders = ['pastrami', 'tuna', 'turkey', 'pastrami', 'roast beef', 'pastrami']

# Create an empty list to hold finished sandwiches.
finished_sandwiches = []

# Check if 'pastrami' appears at least three times.
if sandwich_orders.count('pastrami') >= 3:
    print("Sorry, the deli has run out of pastrami.")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made.
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)