'''IF STATEMENTS'''

# Programming often involves examining a set of conditions and deciding which
# action to take based on those conditions. Python’s if statement allows you to examine
# the current state of a program and respond appropriately to that state.

'''Imagine you have a list of cars and you want to print out the
name of each car. Car names are proper names, so the names of most cars
should be printed in title case. However, the value 'bmw' should be printed
in all uppercase. The following code loops through a list of car names and
looks for the value 'bmw'. Whenever the value is 'bmw', it’s printed in uppercase
instead of title case:'''

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw':
      print(car.upper())
  else:
      print(car.title())


# Conditional Tests-----------------------------------------------------------------------------
'''Checking for Equality - The simplest conditional test checks whether the value of a
variable is equal to the value of interest:'''

car = 'bmw'
if car == 'bmw':
   print('True')
else:
   print('False')

car = 'audi'
if car == 'bmw':
   print('True')
else:
   print('False')


# Ignoring Case When Checking for Equality------------------------------------------------------------
'''Testing for equality is case sensitive in Python'''

car = 'Bmw'
if car == 'bmw':
   print('True')
else:
   print('False')

'''lower() method doesn’t change
the value that was originally stored in car, so you can do this kind of comparison
without affecting the original variable'''

car = 'BMW' # assign the capitalized string 'BMW' to the variable car
if car.lower() == 'bmw': # convert the value of car to lowercase and compare the lowercase value to the string 'BMW'
    print('True') # two strings match, so Python returns True
else:
    print('False')
print(car) # value stored in car has not been affected by the lower() method


# Checking for Inequality-------------------------------------------------------------------------------------
'''When you want to determine whether two values are not equal, you can use
the inequality operator (!=).'''
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")



'''code compares the value of requested_topping to the value 'anchovies'.
If these two values do not match, Python returns True and executes the code
following the if statement. If the two values match, Python returns False and
does not run the code following the if statement'''


# Numerical Comparisons---------------------------------------------------------------------------------------

age = 18
if age == 18:
   print('true')
else:
   print('false')


answer = 17
if answer != 42:
   print("That is not the correct answer. Please try again!")

# using various mathematical operations:

age = 19
if age < 21:
   print('true')
elif age <= 21:
   print('true')
elif age > 21:
   print('false')
elif age >= 21:
   print('false')
else:
   print('Invalid age')


# Checking multiple conditions-------------------------------------------------------------
# Using and to Check Multiple Conditions
age = 22
age_1 = 18
if age >= 21 and age_1 >= 21:
   print('true')
else:
   print('false')


# Using or to Check Multiple Conditions
age = 22
age_1 = 18
if age >= 21 or age_1 >= 21:
   print('true')
else:
   print('false')


# Checking Whether a Value Is in a List
# using 'in' keyword
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print('true')
else:
    print('False')


# Checking Whether a Value Is not in a List
# using 'not' keyword
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
   print(f"{user.title()}, you can post a response if you wish.")