'''Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
'''

# Create a list of people to invite to dinner
guest_list = ["Albert Einstein", "Ada Lovelace", "Nelson Mandela"]

# Iterate through the guest list and print an invitation message for each person
for guest in guest_list:
    print(f"Dear {guest},\nYou are cordially invited to a dinner at my place. I hope you can make it!\n")

print("Invitations sent!")

'''We create a guest_list containing the names of the people we want to invite to dinner.
We use a for loop to iterate through each person in the guest_list.
Inside the loop, we use an f-string to print a personalized invitation message for each guest.
After inviting all guests, the program prints a message indicating that the invitations have been sent.'''