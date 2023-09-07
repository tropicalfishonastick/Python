'''Polling: Use the code in favorite_languages.py (page 96).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.'''

favorite_languages = {
    'alice': 'python',
    'bob': 'java',
    'carol': 'c++',
    'dave': 'python',
    'eve': 'javascript'
}

# Make a list of people who should take the favorite languages poll
people_to_poll = ['alice', 'bob', 'charlie', 'dave', 'frank']

# Loop through the list of people to take the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"Hey, {person.title()}, we invite you to take the poll!")
