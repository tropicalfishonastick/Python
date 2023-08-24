'''Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list.'''

# Create a list of people to invite to dinner
guest_list = ["Albert Einstein", "Ada Lovelace", "Nelson Mandela"]

# Print the name of the guest who can't make it
cannot_attend = "Ada Lovelace"
print(f"Unfortunately, {cannot_attend} can't make it to the dinner.")

# Replace the name of the guest who can't make it
guest_list.remove(cannot_attend)
new_guest = "Marie Curie"
guest_list.append(new_guest)

# Print new invitation messages for the updated guest list
for guest in guest_list:
    print(f"Dear {guest},\nYou are cordially invited to a dinner at my place. I hope you can make it!\n")

print("Invitations sent!")

'''We first print a message indicating that a specific guest ("Ada Lovelace" in this case) can't make it to the dinner.
We then remove the guest who can't make it from the guest_list and add a new guest ("Marie Curie" in this case).
Finally, we use a loop to print new invitation messages for each guest in the updated guest_list.'''
