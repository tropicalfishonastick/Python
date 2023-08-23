import cowsay   # Import the cowsay module
import sys      # Import the sys module for accessing command-line arguments

# Check if there is exactly one command-line argument
if len(sys.argv) == 2:
    # Use the cowsay.cow() function to generate a cow ASCII art with a greeting
    cowsay.cow("hello, " + sys.argv[1])


import cowsay   # Import the cowsay module
import sys      # Import the sys module for accessing command-line arguments

# Check if there is exactly one command-line argument
if len(sys.argv) == 2:
    # Use the cowsay.trex() function to generate a T-Rex ASCII art with a greeting
    cowsay.trex("hello, " + sys.argv[1])

