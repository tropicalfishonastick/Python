'''Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that’s being ordered. Call the function three times, using a different number
of arguments each time.'''
def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

# Call the function with different numbers of arguments
make_sandwich("Ham", "Cheese", "Lettuce")
make_sandwich("Turkey", "Swiss")
make_sandwich("Peanut Butter", "Jelly", "Banana")



'''User Profile:Build a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.'''
def build_profile(first_name, last_name, **kwargs):
    profile = {
        'first_name': first_name,
        'last_name': last_name,
    }
    profile.update(kwargs)
    return profile

# Create a user profile with additional key-value pairs
my_profile = build_profile('John', 'Doe', age=30, city='New York', hobby='Coding')

# Print the user profile
print(my_profile)



'''Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.'''
def make_car(manufacturer, model, **kwargs):
    car_info = {
        'manufacturer': manufacturer,
        'model': model,
    }
    car_info.update(kwargs)
    return car_info

# Create a car dictionary with additional key-value pairs
car = make_car('Subaru', 'Outback', color='blue', tow_package=True)

# Print the car dictionary
print(car)
