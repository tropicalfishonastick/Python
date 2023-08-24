'''Intentional Error: If you haven’t received an index error in one of your programs
yet, try to make one happen. Change an index in one of your programs
to produce an index error. Make sure you correct the error before closing the
program.'''

# Create a list of countries
countries = ["United States", "Canada", "Germany", "Japan", "Australia"]

# Try to find the index of a country not in the list
try:
    index_france = countries.index("France")
    print("Index of France:", index_france)
except ValueError:
    print("France is not in the list.")

# Find the index of a country that is in the list
index_germany = countries.index("Germany")
print("Index of Germany:", index_germany)

'''We attempt to find the index of the country "France" using the index() function. Since "France" is not in the list, it will raise a ValueError index error.
To handle the error, we use a try block along with an except ValueError block. If the error occurs, the program prints a message indicating that "France" is not in the list.
After handling the error, we find the index of "Germany," which is in the list. This part of the code will execute without errors.'''