# personal_message - Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?
person_name = "Eric"
message = f"Hello {person_name}, would you like to learn some Python today?"
print(message)


# Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.
person_name = "John Doe"
print("Lowercase:", person_name.lower())
print("Uppercase:", person_name.upper())
print("Title case:", person_name.title())


# Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never
# tried anything new.”

quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"
print(f'{author} once said, "{quote}"')


# Repeat Exercise 2-5, but this time, represent the famous
# person’s name using a variable called famous_person. Then compose your message
# and represent it with a new variable called message. Print your message.

famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)


# Stripping Names: Use a variable to represent a person’s name, and
# include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

person_name = "\t   John Doe \n"
# Here's a breakdown of the characters in the string:
# \t: This is an escape sequence representing a tab character. It adds horizontal spacing.
# : These are three space characters. They add horizontal spacing.
# John Doe: This is the actual content of the name, without any extra spaces.
# \n: This is an escape sequence representing a newline character. It adds a line break.


print("Original:", person_name)
print("lstrip():", person_name.lstrip())
print("rstrip():", person_name.rstrip())
print("strip():", person_name.strip())


# File Extensions: Python has a removesuffix() method that works exactly
# like removeprefix(). Assign the value 'python_notes.txt' to a variable called
# filename. Then use the removesuffix() method to display the filename without
# the file extension, like some file browsers do.

filename = 'python_notes.txt'
filename_without_extension = filename.removesuffix('.txt')
print("Filename without extension:", filename_without_extension)
