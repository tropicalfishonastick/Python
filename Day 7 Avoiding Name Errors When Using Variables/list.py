bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List-------------------------------------------
# Lists are ordered collections, so you can access any element in a list by
# telling Python the position, or index, of the item desired

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

# format the element 'trek' to look more presentable
# by using the title() method

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())


# Index Positions Start at 0, Not 1 ----------------------------------------------
# Python considers the first item in a list to be at position 0, not position 1
# to access the fourth item in a list, you request the item at index 3
print(bicycles[1])
print(bicycles[3])


# Python has a special syntax for accessing the last element in a list. If you
# ask for the item at index -1, Python always returns the last item in the list
print(bicycles[-1])

# Using Individual Values from a List -------------------------------------------------
# you can use f-strings to create a message based on a value from a list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)