'''Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.'''


# Define the initial tuple of five foods
initial_menu = ('Pasta', 'Salad', 'Pizza', 'Soup', 'Bread')

# Print each food from the initial menu using a for loop
print("Initial Menu:")
for food in initial_menu:
    print(food)

# Try to modify one of the items (Python will raise an error)
try:
    initial_menu[2] = 'Burger'
except TypeError as e:
    print("Error:", e)

# Update the menu by replacing two items
revised_menu = list(initial_menu)  # Convert the tuple to a list to make changes
revised_menu[2] = 'Burger'
revised_menu[4] = 'Fries'
revised_menu = tuple(revised_menu)  # Convert the list back to a tuple

# Print each food from the revised menu using a for loop
print("\nRevised Menu:")
for food in revised_menu:
    print(food)
