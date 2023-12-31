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


# Modifying Elements in a List -----------------------------------------------------------
# say we have a list of motorcycles and the first item in the
# list is 'honda'. We can change the value of this first item after the list has been created
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)


# The append() method makes it easy to build lists dynamically. For example, you can start with an empty list and then add items to the list using a series
# of append() calls. Using an empty list, let’s add the elements 'honda', 'yamaha',and 'suzuki' to the list
cars = []
cars.append('Bugatti')
cars.append('Lexus')
cars.append('GTR')
print(cars)


# Inserting Elements into a List ---------------------------------------------------------------
'''You can add a new element at any position in your list by using the insert()
method. You do this by specifying the index of the new element and the
value of the new item'''
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)


# Removing Elements from a List ----------------------------------------------------------------------
'''You can remove an item according to its
position in the list or according to its value'''

# Removing an Item Using the del Statement :-
'''If you know the position of the item you want to remove from a list, you can
use the del statement'''
'''you can no longer access the value that was removed
from the list after the del statement is used'''

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)


# Removing an Item Using the pop() Method ----------------------------------------------------
'''Sometimes you’ll want to use the value of an item after you remove it from a
list. For example, you might want to get the x and y position of an alien that
was just shot down, so you can draw an explosion at that position. In a web
application, you might want to remove a user from a list of active members
and then add that user to a list of inactive members. The pop() method removes the last item in a list, but it lets you work
with that item after removing it. The term pop comes from thinking of a
list as a stack of items and popping one item off the top of the stack. In this
analogy, the top of a stack corresponds to the end of a list'''
motorcycles = ['honda', 'yamaha', 'suzuki'] # defining list motorcycles
print(motorcycles) # printing list motorcycles
popped_motorcycle = motorcycles.pop() # pop a value from the list, and assign that value to the variable popped_motorcycle
print(motorcycles) # print the list to show that a value has been removed from the list
print(popped_motorcycle)  # print the popped value to prove that we still have access to the value that was removed


''' Imagine that the motorcycles
in the list are stored in chronological order, according to when we owned
them. If this is the case, we can use the pop() method to print a statement
about the last motorcycle we bought:'''
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")


# Popping Items from Any Position in a List ---------------------------------------------------------
'''Remember that each time you use pop(), the item you work with is no
longer stored in the list'''
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")


# Removing an Item by Value -----------------------------------------------------------------remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] # defining the list
print(motorcycles) 
too_expensive = 'ducati' # assign the value 'ducati' to a variable called too_expensive
motorcycles.remove(too_expensive) # use this variable to tell Python which value to remove from the list
print(motorcycles) # value 'ducati' has been removed from the list
print(f"\nA {too_expensive.title()} is too expensive for me.") # is still accessible through the variable too_expensive, allowing us to print a statement about why we removed 'ducati' from the list of motorcycles.


'''The remove() method deletes only the first occurrence of the value you specify. If there’s
a possibility the value appears more than once in the list, you’ll need to use a loop
to make sure all occurrences of the value are removed'''
numbers = [1, 2, 3, 2, 4, 2, 5]

# Value to be removed
value_to_remove = 2

# Loop to remove all occurrences of the value
while value_to_remove in numbers:
    numbers.remove(value_to_remove)

print(numbers)



# Sorting a List Permanently with the sort() Method ---------------------------------------------------------------------
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

'''sort this list in reverse-alphabetical order by passing the
argument reverse=True to the sort() method'''
cars.sort(reverse=True)
print(cars)


# Sorting a List Temporarily with the sorted() Function-----------------------------------------------------------------------
'''The sorted() function lets you display your list
in a particular order, but doesn’t affect the actual order of the list'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)


# Printing a List in Reverse Order--------------------------------------------
print(cars)
cars.reverse()
print(cars)

'''The reverse() method changes the order of a list permanently, but you
can revert to the original order anytime by applying reverse() to the same
list a second time.'''
cars.reverse()
print(cars)


# Finding the Length of a List---------------------------------------------------------------
print(len(cars))

#--------------------------------------------------------------------------------------------
# for loop to print out each name in a list of magicians
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
# thank you message after the for loop, without indentation
print("Thank you, everyone. That was a great magic show!")


#-----------------------------------------------------------------------------------------------
# Using the range() Function
'''Python’s range() function makes it easy to generate a series of numbers'''

for value in range(1, 5):
   print(value)

for value in range(6):
   print(value)

#----------------------------------------------------------------------------------------------
# Using range() to Make a List of Numbers
'''If you want to make a list of numbers, you can convert the results of range()
directly into a list using the list() function'''
numbers = list(range(1, 6))
print(numbers)

# the range() function starts with the value 2 and then adds 2 to that value
even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = [] #empty list called squares
for value in range(1, 11): #Python to loop through each value from 1 to 10 using the range() function
  square = value ** 2 #Inside the loop,the current value is raised to the second power and assigned to the variable square
  squares.append(square) #Each new value of square is then appended to the list squares
print(squares) #when the loop has finished running, the list of squares is printed

#To write this code more concisely------------------------
squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares)



# Simple Statistics with a List of Numbers----------------------------------------------------------------------
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


# List Comprehensions---------------------------------------------------------------------------------------------
'''list comprehension combines the
for loop and the creation of new elements into one line, and automatically
appends each new element'''

squares = [value**2 for value in range(1, 11)]
print(squares)

# Slicing a List-------------------------------------------------------------------------------------------------
'''To make a slice, you specify the index of the first and last elements you want
to work with'''

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])


# Looping Through a Slice----------------------------------------------------------------------------------------------

'''You can use a slice in a for loop if you want to loop through a subset of the
elements in a list. In the next example, we loop through the first three players
and print their names as part of a simple roster'''

print("Here are the first three players on my team:")
for player in players[:3]:
   print(player.title())

# Copying a List-----------------------------------------------------------------------------------------------------

my_foods = ['pizza', 'falafel', 'carrot cake'] #make a list of the foods we like called my_foods
friend_foods = my_foods[:] #make a new list called friend_foods , make a copy of my_foods by asking for a slice of my_foods without specifying any indices
#assign the copy to friend_foods.
#print each list
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

'''To prove that we actually have two separate lists, we’ll add a new food
to each list and show that each list keeps track of the appropriate person’s
favorite foods:'''

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

'''here’s what happens when you try to copy a list without using a slice:'''
'''Instead of assigning a copy of my_foods to friend_foods, we set friend_foods
equal to my_foods. This syntax actually tells Python to associate the new variable
friend_foods with the list that is already associated with my_foods, so now
both variables point to the same list. As a result, when we add 'cannoli' to
my_foods, it will also appear in friend_foods. Likewise 'ice cream' will appear
in both lists, even though it appears to be added only to friend_foods.'''

# This doesn't work:

friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)