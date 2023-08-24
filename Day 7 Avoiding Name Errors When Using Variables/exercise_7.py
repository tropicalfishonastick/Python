# Initialize an empty list to hold user values
user_values = []

# Function to add a value to the list
def add_value(value):
    user_values.append(value)

# Function to display the user values
def display_values():
    print("User values:", user_values)

# Main loop
while True:
    # Get input from the user
    value = input("Enter a value (or 'quit' to exit): ")
    
    # Check if the user wants to quit
    if value.lower() == "quit":
        print("Exiting.")
        break
    else:
        # Add the value to the user_values list
        add_value(value)
        
        # Display the current list of user values
        display_values()



# Explanation:
'''We start by initializing an empty list called user_values. This list will hold the values entered by the user.
The add_value() function takes a parameter value and appends it to the user_values list.
The display_values() function is used to display the current contents of the user_values list.
The main loop while True: runs indefinitely until the user decides to exit.
Inside the loop, we use the input() function to get a value from the user.
We then check if the entered value, when converted to lowercase, is equal to "quit." If it is, we print an exit message and break out of the loop to end the program.
If the entered value is not "quit," we call the add_value() function to add the value to the user_values list.
After adding the value, we call the display_values() function to show the current list of user values.
This code allows the user to enter values one by one, adds those values to the user_values list, and displays the list after each input. The user can exit the loop by typing "quit."'''