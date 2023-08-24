'''More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list'''

# Create the original list of people to invite to dinner
guest_list = ["Albert Einstein", "Ada Lovelace", "Nelson Mandela"]

# Print a message about finding a bigger table
print("Great news! We found a bigger dinner table, so we can invite more guests!")

# Insert new guests at the beginning, middle, and end of the list
guest_list.insert(0, "Marie Curie")    # Insert at the beginning
guest_list.insert(len(guest_list)//2, "Isaac Newton")  # Insert in the middle
guest_list.append("Galileo Galilei")   # Append at the end

# Print new invitation messages for the updated guest list
for guest in guest_list:
    print(f"Dear {guest},\nYou are cordially invited to a dinner at my place. I hope you can make it!\n")

print("Invitations sent!")

'''We start with the original list of guests from Exercise 3-4 or 3-5.
We print a message announcing that a bigger table has been found.
We use the insert() method to add new guests at different positions in the list. We insert one guest at the beginning, one in the middle, and one at the end of the list.
Finally, we use a loop to print new invitation messages for each person in the updated guest_list.'''
