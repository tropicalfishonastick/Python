# 3. Rollback Operations - Maintaining Data Consistency
# open multiple files as part of a transaction. If an exception occurs (e.g., a ZeroDivisionError), 
# we handle the exception and perform a rollback operation (e.g., deleting file1.txt) to maintain data consistency.
try:
    # Open multiple files as part of a transaction
    with open("file1.txt", "w") as file1, open("file2.txt", "w") as file2:
        # Write data to file1
        file1.write("Data for file1")
        
        # Intentionally raise an exception to simulate an error
        1 / 0
        
        # Write data to file2 (this won't execute due to the exception)
        file2.write("Data for file2")
except ZeroDivisionError as e:
    # Handle the exception
    print(f"Error: {e}")
    
    # Perform a rollback operation (e.g., delete file1)
    import os
    os.remove("file1.txt")
else:
    # Commit the transaction (in this case, there's nothing to commit)
    print("Transaction completed successfully.")

"""Rollback Operations: In some cases, when working with multiple files as part of a transaction or critical process, 
you might need to perform a rollback operation if an error occurs. 
Exception handling allows you to detect errors and execute rollback logic to maintain data consistency."""