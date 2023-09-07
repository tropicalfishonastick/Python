'''Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user.
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.'''

# List of usernames
usernames = ['admin', 'jaden', 'emma', 'oliver', 'sophia']

# Loop through the list and print greetings
for username in usernames:
    if username == 'admin':  # Check if the current username is 'admin'
        print(f"Hello {username}, would you like to see a status report?")
    else:  # If the username is not 'admin'
        print(f"Hello {username.capitalize()}, thank you for logging in again.")
