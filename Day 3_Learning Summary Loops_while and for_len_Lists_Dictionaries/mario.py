# Print a single "#" character three times
print("#")
print("#")
print("#")

# Loop three times and print "#" each time
for _ in range(3):
    print("#")

# Define the main function
def main():
    # Call the print_column function with a height of 3
    print_column(3)

# Define a function to print a column of "#" characters with a given height
def print_column(height):
    for _ in range(height):
        print("#")

# Call the main function
main()

# Redefine the main function
def main():
    # Call the print_row function with a width of 4
    print_row(4)

# Define a function to print a row of "?" characters with a given width
def print_row(width):
    print("?" * width)

# Call the main function
main()

# Redefine the main function
def main():
    # Call the print_square function with a size of 3
    print_square(3)

# Define a function to print a square of "#" characters with a given size
def print_square(size):
    # Loop through each row
    for i in range(size):
        # Loop through each brick in the row
        for j in range(size):
            # Print a "#" character (brick)
            print("#", end="")
        # Print a blank line to move to the next row
        print()

# Call the main function
main()

# Redefine the main function
def main():
    # Call the print_square function with a size of 3
    print_square(3)

# Redefine the print_square function to call the print_row function for each row
def print_square(size):
    # Loop through each row
    for i in range(size):
        # Call the print_row function to print a row of "#" characters
        print_row(size)

# Define a function to print a row of "#" characters with a given width
def print_row(width):
    print("#" * width)

# Call the main function
main()
