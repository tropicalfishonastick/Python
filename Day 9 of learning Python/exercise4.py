'''In a mapping project, you might want to
check whether a submitted location already exists in a list of known locations'''

# use a similar approach as with the username example to check whether a submitted location already exists in a list of known locations

# List of known locations
known_locations = ['New York', 'Los Angeles', 'Chicago', 'Houston']

# Function to check if a location already exists
def is_location_known(new_location, known_locations):
    # Convert all known locations to lowercase
    lowercase_known = [location.lower() for location in known_locations]
    
    # Check if the lowercase version of the new location is in the list of lowercase known locations
    return new_location.lower() in lowercase_known

# Example usage
submitted_location = input("Enter a new location: ")  # Prompt the user for a new location
if is_location_known(submitted_location, known_locations):  # Call the function to check existence
    print("Location already exists in the list.")
else:
    known_locations.append(submitted_location)  # Add the new location to the list of known locations
    print("Location is new and added.")


'''the process is similar to the username code:

We have a list called known_locations containing some example known locations.
The function is_location_known takes a new location and the list of known locations as parameters.
Inside the function:
We create a new list lowercase_known using a list comprehension. This list contains the lowercase version of each known location.
The function then checks if the lowercase version of the new location is present in the lowercase_known list. If it's present, the location is considered known and the function returns True. If it's not present, the location is considered new and the function returns False.
In the example usage section:
We prompt the user to enter a new location using the input function.
We call the is_location_known function with the new location and the list of known locations as arguments.
If the function returns True, indicating that the location is known, we print a message saying it already exists in the list.
If the function returns False, indicating that the location is new, we add the new location to the list of known locations and print a success message.
This approach allows you to efficiently check for the existence of a location in a case-insensitive manner, similar to the username example.'''