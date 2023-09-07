'''Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.
'''
# Prompt the user for their name
user_name = input("Please enter your name: ")

# Write the user's name to a file called guest.txt
with open("guest.txt", "w") as file:
    file.write(user_name)

# This program prompts the user for their name, reads the input, and then writes the name to a file called guest.txt.

'''Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, and 
then write these names to a file called guest_book.txt. Make sure each entry appears on a new line in the file.
'''
# Create an empty list to store guest names
guest_names = []

# Continuously prompt users for their name until they enter 'quit'
while True:
    user_name = input("Please enter your name (or 'quit' to exit): ")

    # Check if the user wants to quit
    if user_name.lower() == 'quit':
        break

    # Add the user's name to the list
    guest_names.append(user_name)

# Write the collected names to a file called guest_book.txt
with open("guest_book.txt", "w") as file:
    for name in guest_names:
        file.write(name + "\n")


# This program uses a while loop to continuously prompt users for their names and collects them in a list. 
# When the user enters "quit," the loop exits, and it writes the collected names to a file called guest_book.txt, with each name on a new line.
# Both programs use the with open(...) statement to ensure proper file handling by automatically closing the file when done.
# Adjust the file names as needed for your use case.