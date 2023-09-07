# 1. Graceful Error Handling - Handling File Not Found
#  we try to open a file that does not exist. If a FileNotFoundError occurs, 
# the code inside the except block is executed to handle the error gracefully.
try:
    # Attempt to open a non-existent file
    with open("non_existent_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError as e:
    # Handle the "File Not Found" error gracefully
    print(f"Error: {e}")
else:
    # This block executes if there are no exceptions
    print("File read successfully.")


"""Graceful Error Handling: When working with multiple files, there's a higher likelihood of encountering errors, such as file not found, 
permission denied, or file corruption. 
Using try-except blocks allows you to catch these errors and handle them gracefully instead of crashing your program."""