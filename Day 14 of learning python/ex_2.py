'''Login Attempts: Add an attribute called login_attempts to your User class
from. Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.'''
class User:
    def __init__(self, first_name, last_name, username, email):
        # Initialize user attributes
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        # Initialize login_attempts to 0 when a user is created
        self.login_attempts = 0

    def describe_user(self):
        # Print user information
        print(f"Full Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        # Greet the user
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        # Increment the login_attempts by 1
        self.login_attempts += 1

    def reset_login_attempts(self):
        # Reset the login_attempts to 0
        self.login_attempts = 0

# Create an instance of the User class
user1 = User("John", "Doe", "johndoe", "johndoe@example.com")

# Increment login_attempts several times
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Print the current value of login_attempts (should be 3)
print(f"Login Attempts: {user1.login_attempts}")

# Reset login_attempts
user1.reset_login_attempts()

# Print login_attempts again (should be 0 after resetting)
print(f"Login Attempts (after reset): {user1.login_attempts}")
