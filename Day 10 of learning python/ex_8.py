'''Pets: Make several dictionaries, where each dictionary represents a different
pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet.'''

# Create a list of dictionaries, each representing a pet
pets = [
    {'kind': 'dog', 'owner': 'Alice'},
    {'kind': 'cat', 'owner': 'Bob'},
    {'kind': 'parrot', 'owner': 'Carol'}
]

# Loop through the list of pets and print information about each pet
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}")
    print("\n")
