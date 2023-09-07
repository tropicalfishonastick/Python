# 4. Logging and Debugging - Logging Error Details
# configure logging to write error details to a log file. When an exception occurs (e.g., due to an invalid file mode), 
# the error details, including the exception message and traceback, are logged to the error_log.txt file for debugging and troubleshooting.
import logging

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

try:
    # Attempt to open a file with an invalid mode
    with open("invalid_mode.txt", "xyz") as file:
        pass
except Exception as e:
    # Log the error details to a log file
    logging.error(f"Error: {e}", exc_info=True)

"""
Logging and Debugging: Exception handling allows you to log error details, which can be immensely helpful for debugging and 
troubleshooting when working with multiple files.
You can log exceptions, their messages, and even the file or line number where the error occurred."""