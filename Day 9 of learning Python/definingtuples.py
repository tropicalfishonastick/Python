# define a tuple, you can access individual elements by using each item’s index------------------------
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping Through All Values in a Tuple---------------------------------------------------------------
# using a for loop:
for dimension in dimensions:
    print(dimension)

# Writing Over a Tuple------------------------------------------------------------------------------
'''you can’t modify a tuple, you can assign a new value to a variable
that represents a tuple'''
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
   print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
   print(dimension)

'''When compared with lists, tuples are simple data structures. Use them
when you want to store a set of values that should not be changed throughout
the life of a program'''