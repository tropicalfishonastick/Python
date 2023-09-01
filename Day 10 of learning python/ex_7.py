'''People: Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionaries
in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.'''

# Define dictionaries for three people
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

person2 = {
    'first_name': 'Alice',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}

person3 = {
    'first_name': 'Bob',
    'last_name': 'Johnson',
    'age': 35,
    'city': 'Chicago'
}

# Store the dictionaries in a list called 'people'
people = [person1, person2, person3]

# Loop through the list of people and print their information
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print("\n")
