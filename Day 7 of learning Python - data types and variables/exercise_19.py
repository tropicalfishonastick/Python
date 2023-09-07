'''Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a
slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to
print the last three items in the list.'''

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# Print the first three items in the list
print("The first three items in the list are:")
print(my_foods[:3])

# Print three items from the middle of the list

'''middle_index = len(my_foods) // 2: This line calculates the index of the middle element in the my_foods list. Here's what each part does:

len(my_foods) returns the number of elements in the my_foods list, which is the total length of the list.
// is the floor division operator. It divides the length of the list by 2 and rounds down to the nearest integer. This gives us the index of the middle element in the list.
print("Three items from the middle of the list are:"): This line simply prints the message "Three items from the middle of the list are:" to provide context for the upcoming output.

print(my_foods[middle_index:middle_index + 3]): This line uses slicing to extract and print three items from the middle of the list. Here's what each part of the slicing does:

my_foods[middle_index:middle_index + 3] specifies a slice of the my_foods list.
middle_index is the starting index of the slice, which is the index of the middle element in the list.
middle_index + 3 is the ending index of the slice. Since we want to print three items, we add 3 to the middle index to include the elements up to the middle index + 2.
In summary, the code calculates the index of the middle element in the list, then uses slicing to extract and print three items from that calculated middle index. This allows you to print a subset of the list that includes three elements from the middle portion'''

middle_index = len(my_foods) // 2
print("Three items from the middle of the list are:")
print(my_foods[middle_index:middle_index + 3])

# Print the last three items in the list
print("The last three items in the list are:")
print(my_foods[-3:])
