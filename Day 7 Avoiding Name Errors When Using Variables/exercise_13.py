'''Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once'''

# Create a list of countries
countries = ["United States", "Canada", "France", "Japan", "Australia"]

# Print the original list
print("Original list:", countries)

# Use append() to add a new country
countries.append("Brazil")
print("List after appending:", countries)

# Use insert() to insert a country at a specific position
countries.insert(2, "Germany")
print("List after inserting:", countries)

# Use remove() to remove a specific country
countries.remove("France")
print("List after removing:", countries)

# Use pop() to remove and return the last country
popped_country = countries.pop()
print("List after popping:", countries)
print("Popped country:", popped_country)

# Use sort() to sort the list in alphabetical order
countries.sort()
print("List after sorting:", countries)

# Use reverse() to reverse the order of the list
countries.reverse()
print("List after reversing:", countries)

# Use len() to get the length of the list
num_countries = len(countries)
print("Number of countries:", num_countries)

# Use sorted() to get a sorted version of the list without modifying the original list
sorted_countries = sorted(countries)
print("Sorted countries:", sorted_countries)

# Use index() to find the index of a specific country
index_japan = countries.index("Japan")
print("Index of Japan:", index_japan)

# Use count() to count the occurrences of a specific country
count_canada = countries.count("Canada")
print("Count of Canada:", count_canada)

# Use clear() to empty the list
countries.clear()
print("List after clearing:", countries)

''' a list of countries and applied various functions and methods introduced in the chapter:
append() to add an item to the end of the list.
insert() to insert an item at a specific position.
remove() to remove a specific item.
pop() to remove and return the last item.
sort() to sort the list in place.
reverse() to reverse the order of the list.
len() to get the length of the list.
sorted() to get a sorted version of the list without modifying the original.
index() to find the index of a specific item.
count() to count the occurrences of a specific item.
clear() to empty the list.'''

#----------------------------------------------------------------------------------------------------

