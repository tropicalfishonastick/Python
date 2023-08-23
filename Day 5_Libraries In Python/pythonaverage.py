# Import the 'sys' module to access command-line arguments
import sys

# Check if there are enough command-line arguments
if len(sys.argv) < 2:
    print("Usage: python script_name.py your_name")
else:
    print("hello, my name is", sys.argv[1])


# Import the 'sys' module to access command-line arguments
import sys

try:
    # Try to print a message using the second command-line argument
    print("hello, my name is", sys.argv[1])
except IndexError:
    # If an IndexError occurs (i.e., not enough command-line arguments provided)
    # Print an error message indicating too few arguments
    print("Too few arguments")


import sys

# Check the number of command-line arguments
if len(sys.argv) < 2:
    # If there are fewer than 2 arguments (including the script name),
    # print an error message indicating too few arguments
    print("Too few arguments")
elif len(sys.argv) > 2:
    # If there are more than 2 arguments (including the script name),
    # print an error message indicating too many arguments
    print("Too many arguments")
else:
    # If exactly 2 arguments (script name and one additional argument) are provided,
    # print a message including the provided argument (name)
    print("hello, my name is", sys.argv[1])


import sys

# Check the number of command-line arguments
if len(sys.argv) < 2:
    # If there are fewer than 2 arguments (including the script name),
    # exit the script with an error message indicating too few arguments
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    # If there are more than 2 arguments (including the script name),
    # exit the script with an error message indicating too many arguments
    sys.exit("Too many arguments")

# If the number of arguments is exactly 2 (script name and one additional argument),
# print a message including the provided argument (name)
print("hello, my name is", sys.argv[1])
