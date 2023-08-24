'''Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (pages 41–42), use len() to print a message indicating the number
of people you’re inviting to dinner'''

# Create the original list of people to invite to dinner
guest_list = ["Albert Einstein", "Ada Lovelace", "Nelson Mandela", "Marie Curie", "Isaac Newton", "Galileo Galilei"]

# Print the number of people you're inviting to dinner
num_guests = len(guest_list)
print(f"There are {num_guests} people invited to dinner.")

'''We start with the extended guest list from one of the previous exercises.
We use the len() function to calculate the number of people in the guest_list.
We then use an f-string to print a message indicating the number of people invited to dinner.'''

#-----------------------------------------------------------------------------------------------------