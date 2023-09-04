'''Modifying a List in a Function'''
# When you pass a list to a function, the function can modify the list. Any
# changes made to the list inside the function’s body are permanent, allowing
# you to work efficiently even when you’re dealing with large amounts of data.
# Consider a company that creates 3D printed models of designs that
# users submit. Designs that need to be printed are stored in a list, and after
# being printed they’re moved to a separate list. The following code does this
# without using functions

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
   current_design = unprinted_designs.pop()
   print(f"Printing model: {current_design}")
   completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
   print(completed_model)

# alternate way
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)