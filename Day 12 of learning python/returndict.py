'''RETURNING A DICTIONARY'''
# the following function takes in parts of a name and returns a dictionary representing a person:
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

# extend this function to accept optional values
def build_person(first_name, last_name, age=None): # NONE used when a variable has no specific value assigned to it. None as a placeholder value. In conditional tests, None evaluates to False
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
       person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)