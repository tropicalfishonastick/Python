'''T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.'''

def make_shirt(size, message):
    print(f"The shirt is size {size} and has the message: '{message}'")

# Calling the function using positional arguments
make_shirt("medium", "Hello, World!")

# Calling the function using keyword arguments
make_shirt(size="large", message="Python Developer")


'''Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.'''

def make_shirt(size="large", message="I love Python"):
    print(f"The shirt is size {size} and has the message: '{message}'")

# Making a large shirt with the default message
make_shirt()

# Making a medium shirt with the default message
make_shirt(size="medium")

# Making a shirt of any size with a different message
make_shirt(size="small", message="Python is awesome!")


'''Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.'''

def describe_city(city, country="USA"):
    print(f"{city} is in {country}")

# Call the function for three different cities
describe_city("New York")
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
