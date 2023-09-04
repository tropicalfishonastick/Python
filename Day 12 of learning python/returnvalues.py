'''RETURN VALUES'''

# Returning a Simple Value
def get_formatted_name(first_name, last_name):
   """Return a full name, neatly formatted."""
   full_name = f"{first_name} {last_name}"
   return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an Argument Optional
'''to expand get_formatted_name() to handle middle names as well. A first attempt to include middle names might look like this:'''

def get_formatted_name(first_name, middle_name, last_name):
   """Return a full name, neatly formatted."""
   full_name = f"{first_name} {middle_name} {last_name}"
   return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

'''But middle names aren’t always needed, 
and this function as written would not work if you tried to call it with only a first name and a last name.
To make the middle name optional, we can give the middle_name argument an empty default value 
and ignore the argument unless the user provides a value. To make get_formatted_name() work without a middle name,
we set the default value of middle_name to an empty string and move it to the end of the list of parameters:'''

def get_formatted_name(first_name, last_name, middle_name=''): # middle name is optional, so it’s listed last in the definition, and its default value is an empty string.
    """Return a full name, neatly formatted."""
    if middle_name:
       full_name = f"{first_name} {middle_name} {last_name}"
    else:
       full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)