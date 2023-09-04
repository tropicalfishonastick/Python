'''Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.'''
# main_program.py

# Importing approaches
import printing_functions
from printing_functions import print_models
from printing_functions import show_completed_models as show_models
import printing_functions as pf
from printing_functions import *

# Call the function using different approaches
unprinted_designs = ['design4', 'design5', 'design6']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
print_models(unprinted_designs, completed_models)
show_models(completed_models)
pf.print_models(unprinted_designs, completed_models)
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
