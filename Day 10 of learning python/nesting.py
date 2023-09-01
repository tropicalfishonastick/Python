'''NESTING-------------------------------------------------------------------------------------------------------------------------'''

# to store multiple dictionaries in a list, or a list of items as a value in a dictionary. This is called nesting. You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary

# 1) A List of Dictionaries--------------------------------------------------------------------
# make a list of aliens in which each alien is a dictionary of information about that alien.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


# another example
# Make an empty list for storing aliens.
# this code creates a list of 30 green aliens (represented as dictionaries) and displays information about the first 5 of them. It also provides a count of the total number of aliens created.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

'''
aliens = []: This line initializes an empty list called aliens. This list will be used to store information about green aliens.

for alien_number in range(30):: This for loop runs 30 times, iterating from alien_number 0 to 29. It's meant to create 30 green aliens.

new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}: Inside the loop, a new dictionary named new_alien is created for each iteration. Each dictionary represents a green alien and has three key-value pairs: 'color' is set to 'green', 'points' is set to 5, and 'speed' is set to 'slow'.

aliens.append(new_alien): After creating a new alien dictionary, it is appended to the aliens list. This adds the dictionary to the end of the list.

for alien in aliens[:5]:: This for loop iterates over the first 5 aliens in the aliens list using slicing (aliens[:5]). It is used to display information about the first 5 green aliens.

print(alien): Within the loop, each alien dictionary is printed, showing its color, points, and speed.

print("..."): After printing information about the first 5 aliens, an ellipsis ("...") is printed to indicate that there are more aliens not shown in this part of the output.

print(f"Total number of aliens: {len(aliens)}"): Finally, this line prints the total number of green aliens created in the aliens list. It uses the len() function to count the number of elements (dictionaries) in the aliens list.
'''

# use a for loop and an if statement to change the color of the aliens
# first three aliens to yellow, medium-speed aliens worth 10 points each

aliens = [] # creating a list called aliens
# Make 30 green aliens.

'''for alien_number in range(30):: This for loop iterates 30 times, from alien_number 0 to 29, and is intended to create 30 green aliens.
new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}: Inside the loop, a new dictionary named new_alien is created for each iteration. Each dictionary represents a green alien and has three key-value pairs: 'color' is set to 'green', 'points' is set to 5, and 'speed' is set to 'slow'.
aliens.append(new_alien): After creating a new alien dictionary, it is appended to the aliens list. This adds the dictionary to the end of the list.'''

for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

'''This loop iterates over the first three aliens in the aliens list (aliens at index 0, 1, and 2).
It checks if the color of each alien is 'green' using if alien['color'] == 'green':.
If the condition is met (the alien is green), it updates the alien's attributes to change its color to 'yellow', speed to 'medium', and points to 10. This effectively transforms the first three green aliens into yellow ones with different characteristics.'''

for alien in aliens[:3]:
    if alien['color'] == 'green':
       alien['color'] = 'yellow'
       alien['speed'] = 'medium'
       alien['points'] = 10

'''t loops through the first 5 aliens in the aliens list and prints information about each alien, which now includes the modified attributes (color, speed, and points).
After printing information about the first 5 aliens, it prints an ellipsis ("...") to indicate that there are more aliens not shown in this part of the output'''

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# 2) A List in a Dictionary----------------------------------------------------------------------------------------------
# Store information about a pizza being ordered.
# This line creates a dictionary named pizza with two key-value pairs
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
"with the following toppings:")
# for loop to print each topping from the 'toppings' list:
# iterates through each item (topping) in the pizza['toppings'] list.
for topping in pizza['toppings']:
    print(f"\t{topping}")


# another example
# value associated with each name in favorite_languages is now a list
favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell'],
}

# another for loop 2 to run through each person’s list of favorite languages.
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
# loop through the dictionary, use the variable name languages to hold each value from the dictionary, each value will be a list
for language in languages:
    print(f"\t{language.title()}")


# 3) A Dictionary in a Dictionary---------------------------------------------------------------------------------------------

# define a dictionary called users with two keys: one each for the usernames 'aeinstein' and 'mcurie'
# value associated with each key is a dictionary that includes each user’s first name, last name, and location.

users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
# loop through the users dictionary
# Python assigns each key to the variable username, and the dictionary associated with each username is assigned to the variable user_info. Once inside the main dictionary loop, we print the username
for username, user_info in users.items():
  print(f"\nUsername: {username}")

  # start accessing the inner dictionary
  # variable user_info, which contains the dictionary of user information, has three keys: 'first', 'last', and 'location'
  full_name = f"{user_info['first']} {user_info['last']}"
  location = user_info['location']
  print(f"\tFull name: {full_name.title()}")
  print(f"\tLocation: {location.title()}")