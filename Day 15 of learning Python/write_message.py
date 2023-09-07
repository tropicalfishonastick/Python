# Writing to a File
# 1) Writing a Single Line
from pathlib import Path
path = Path('programming.txt')
path.write_text("I love programming.")

'''This program has no terminal output, but if you open the file programming.txt, you’ll see one line. "I love programming."'''

'''When storing numerical data in a text file, 
you should convert the data to string format using the str() function or by using f-strings (formatted strings). Here's how you can do it'''
'''convert each item in the numerical_data list to a string using a list comprehension and then write each string to the text file.'''
# Sample numerical data
numerical_data = [42, 3.14159, 100, 7.5]

# Convert the numerical data to strings
string_data = [str(item) for item in numerical_data]

# Open a text file for writing
with open("numerical_data.txt", "w") as file:
    # Write the converted data to the file
    for item in string_data:
        file.write(item + "\n")


# Using f-strings (formatted strings):
# Sample numerical data
numerical_data = [42, 3.14159, 100, 7.5]

# Open a text file for writing
with open("numerical_data.txt", "w") as file:
    # Write the data to the file using f-strings
    for item in numerical_data:
        file.write(f"{item}\n")

'''directly write the numerical data to the file as strings using f-strings within the write method.s'''


# Writing Multiple Lines
from pathlib import Path
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path = Path('programming.txt')
path.write_text(contents)