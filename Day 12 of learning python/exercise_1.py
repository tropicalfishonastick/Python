'''Message: Write a function called display_message() that prints one sentence
telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.

Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.'''

# Define a function called display_message() to print a message about what you're learning.
def display_message():
    message = "In this chapter, I'm learning about creating and using functions in Python."
    print(message)

# Call the display_message() function to display the message.
display_message()

# Define a function called favorite_book() that takes a parameter 'title'.
def favorite_book(title):
    # Inside the function, create a message that includes the 'title' parameter.
    message = f"One of my favorite books is {title}."
    print(message)

# Call the favorite_book() function with a specific book title as an argument.
favorite_book("Rich Dad Poor Dad")
