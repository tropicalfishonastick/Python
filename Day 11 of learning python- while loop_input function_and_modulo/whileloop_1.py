'''Moving Items from One List to Another'''

# Consider a list of newly registered but unverified users of a website. 
# After we verify these users, how can we move them to a separate list of confirmed users? 
# One way would be to use a while loop to pull users from the list of unconfirmed users as we verify them and then add them to a separate list of confirmed users. 
# Here’s what that code might look like:'''

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

'''We begin with a list of unconfirmed users (Alice, Brian, and Candace) and an empty list to hold confirmed users. 
The while loop runs as long as the list unconfirmed_users is not empty. 
Within this loop, the pop() method removes unverified users one at a time from the end of unconfirmed_users.
Because Candace is last in the unconfirmed_users list, her name will be the first to be removed, assigned to current_user, and added to the confirmed_users list 4. Next is Brian, then Alice.
We simulate confirming each user by printing a verification message and then adding them to the list of confirmed users. As the list of unconfirmed users shrinks, the list of confirmed users grows. When the list of unconfirmed users is empty, the loop stops and the list of confirmed users
is printed'''