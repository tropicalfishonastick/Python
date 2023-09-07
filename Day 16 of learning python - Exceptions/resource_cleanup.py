# 2. Resource Cleanup - Ensuring Proper Resource Release
# raise a ZeroDivisionError to simulate an error condition. 
# The finally block ensures that the file is closed properly, even if an exception occurs during file operations.
try:
    # Open a file for writing
    with open("resource_example.txt", "w") as file:
        # Perform some operations with the file
        file.write("Hello, world!")
        # Intentionally raise an exception
        1 / 0
except ZeroDivisionError as e:
    # Handle the exception
    print(f"Error: {e}")
finally:
    # Ensure that the file is closed, even if an exception occurs
    if 'file' in locals():
        file.close()

"""Resource Cleanup: Exception handling ensures that resources, like open file handles, are properly released when errors occur. 
This prevents resource leaks and ensures that the files are closed even if an exception is raised during file operations."""