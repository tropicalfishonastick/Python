# Looping Through a Dictionary===========================================================================================================

'''1) Looping Through All Key-Value Pairs----------------------------------------------------------------------------------------------'''

# dictionary designed to store information about a user on a website. following dictionary would store one person’s username, first name, and last name
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
   print(f"\nKey: {key}")
print(f"Value: {value}")

# another example
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


# Looping Through All the Keys in a Dictionary
'''The keys() method is useful when you don’t need to work with all of the values
in a dictionary.This for loop tells Python to pull all the keys from the dictionary favorite
_languages and assign them one at a time to the variable name'''

# here i use the keys() method explicitly
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())


'''Looping through the keys is actually the default behavior when looping
through a dictionary, so this code would have exactly the same output if you
wrote:'''
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name in favorite_languages:
    print(name.title())

# make a list of friends that we want to print a message to
friends = ['phil', 'sarah']

# Inside the loop, we print each person’s name
for name in favorite_languages.keys():
  print(f"Hi {name.title()}.")

  # Then we check whether the name we’re working with is in the list friends
  if name in friends:
    # If it is, we determine the person’sfavorite language using the name of the dictionary and the current value of name as the key
    language = favorite_languages[name].title()

    # print a special greeting, including a reference to their language of choice.
    print(f"\t{name.title()}, I see you love {language}!")

'''You can also use the keys() method to find out if a particular person
was polled. This time, let’s find out if Erin took the poll:'''

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


''' 2) Looping Through a Dictionary’s Keys in a Particular Order----------------------------------------------------------------------------'''
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
# wrapped the sorted() function around the dictionary.keys() method
'''tells Python to get all the keys in the dictionary and sort them before starting
the loop. The output shows everyone who took the poll, with the names displayed
in order'''
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


'''Looping Through All Values in a Dictionary-----------------------------------------------------------------------'''

# If you are primarily interested in the values that a dictionary contains, you can use the values() method to return a sequence of values without any keys

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# ------------------------------------------------------------------------------------------------------------------------------------
# To see each language chosen without repetition, we can use a set. A set is a collection in which each item must be unique
# wrap set() around a collection of values that contains duplicate items, Python identifies the unique items in the collection and builds a set from those items
# result is a nonrepetitive list of languages
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())