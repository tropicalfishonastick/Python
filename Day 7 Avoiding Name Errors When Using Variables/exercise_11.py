'''Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.'''

# Create the original list of people to invite to dinner
guest_list = ["Albert Einstein", "Ada Lovelace", "Nelson Mandela", "Marie Curie", "Isaac Newton", "Galileo Galilei"]

# Print a message about the smaller table
print("Oops! The new dinner table won't arrive in time, so we can only invite two people for dinner.")

# Use pop() to remove guests until only two names remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry, {removed_guest}, we can't invite you to dinner.")

# Print invitation messages for the remaining two guests
for remaining_guest in guest_list:
    print(f"Dear {remaining_guest},\nYou are still invited to a dinner at my place. I hope you can make it!\n")

# Use del to remove the last two names from the list
del guest_list[:]
print("Guest list is now empty:", guest_list)

'''We start with the extended guest list from the previous exercise.
We print a message indicating that due to the smaller table, only two people can be invited.
We use a while loop with the pop() method to remove guests one at a time until only two names remain in the list. For each removed guest, we print a message apologizing for not being able to invite them.
After the loop, we print invitation messages for the two remaining guests.
We use the del statement to remove all names from the guest_list, effectively emptying the list. We then print the list to confirm that it's empty.'''

#------------------------------------------------------------------------------------------------------------------------------