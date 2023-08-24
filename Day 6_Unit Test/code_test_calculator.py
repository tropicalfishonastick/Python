# Import the 'square' function from a module named 'calculator'
import sys
sys.path.append(r"c:\Users\Ayushi Tripathi\OneDrive\Documents\Github\Python\Day 6_Unit Test")

from calculator import square

# Define the main function
def main():
    # Call the 'test_square' function to perform tests
    test_square()

# Define a function to test the 'square' function
def test_square():
    # Check if the result of 'square(2)' is not equal to 4
    if square(2) != 4:
        print("2 squared was not 4")
    
    # Check if the result of 'square(3)' is not equal to 9
    if square(3) != 9:
        print("3 squared was not 9")

# Check if the current script is being run as the main program
if __name__ == "__main__":
    # If the script is being run as the main program, execute the 'main' function
    main()
