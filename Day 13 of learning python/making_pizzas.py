import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Importing Specific Functions
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Function an Alias - alias—an alternate name similar to a nickname for the function
'''Here we give the function make_pizza() an alias, mp(), by importing make
_pizza as mp. The as keyword renames a function using the alias you provide'''
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module
'''Python to import every function in a module by using the asterisk (*) operator:'''
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')