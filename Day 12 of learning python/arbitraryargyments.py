'''Passing an Arbitrary Number of Arguments'''
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

'''The asterisk in the parameter name *toppings tells Python to make a tuple called toppings, containing all the values this function receives.
The print() call in the function body produces output showing that Python can handle a function call with one value and a call with three values. 
It treats the different calls similarly. 
Note that Python packs the arguments into a tuple, even if the function receives only one value'''

# Now we can replace the print() call with a loop that runs through the list of toppings and describes the pizza being ordered:
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# This syntax works no matter how many arguments the function receives