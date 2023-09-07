'''a site might use a conditional test like this to ensure that every user has a truly unique username, not just a variation on
the capitalization of another person’s username. When someone submits a
new username, that new username is converted to lowercase and compared
to the lowercase versions of all existing usernames. During this check, a username
like 'John' will be rejected if any variation of 'john' is already in use.'''

# using case-insensitive comparison is a common technique to ensure that usernames are unique regardless of capitalization

# List of existing usernames
existing_usernames = ['alice', 'bob', 'carol', 'dave']

# Function to check if a new username is unique
def is_username_unique(new_username, existing_usernames):
    # Convert all existing usernames to lowercase
    lowercase_existing = [username.lower() for username in existing_usernames]
    
    # Check if the lowercase version of the new username is not in the list of lowercase existing usernames
    return new_username.lower() not in lowercase_existing

# Example usage
new_username = input("Enter a new username: ")  # Prompt the user for a new username
if is_username_unique(new_username, existing_usernames):  # Call the function to check uniqueness
    existing_usernames.append(new_username)  # Add the new username to the list of existing usernames
    print("Username is unique and added.")
else:
    print("Username is already taken.")


'''how the code works:

We have a list called existing_usernames containing some example usernames.
The function is_username_unique takes a new username and the list of existing usernames as parameters.
Inside the function:
We create a new list lowercase_existing using a list comprehension. This list contains the lowercase version of each existing username.
This step ensures that we can perform case-insensitive comparison.
The function then checks if the lowercase version of the new username is not present in the lowercase_existing list. If it's not present, the username is considered unique and the function returns True. If it is present, the username is considered taken and the function returns False.
In the example usage section:
We prompt the user to enter a new username using the input function.
We call the is_username_unique function with the new username and the list of existing usernames as arguments.
If the function returns True, indicating that the username is unique, we add the new username to the list of existing usernames and print a success message.
If the function returns False, we print a message indicating that the username is already taken.



'''