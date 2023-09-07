'''No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message
is printed'''

# List of usernames
usernames = []  # You can remove all the usernames from the list

# Check if the list is empty
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username.capitalize()}, thank you for logging in again.")
else:
    print("We need to find some users!")
