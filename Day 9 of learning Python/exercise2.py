'''Code Review: Choose three of the programs you’ve written in this chapter
and modify each one to comply with PEP 8.
• Use four spaces for each indentation level. Set your text editor to insert four
spaces every time you press the TAB key, if you haven’t already done so
(see Appendix B for instructions on how to do this).
• Use less than 80 characters on each line, and set your editor to show a
vertical guideline at the 80th character position.
• Don’t use blank lines excessively in your program files.'''


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
