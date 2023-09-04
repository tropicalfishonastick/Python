'''Users: Make a class called User. 
Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.'''
class User:
    # The __init__() method initializes user profile attributes
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    # A method called describe_user() prints a summary of user information
    def describe_user(self):
        print(f"User Information:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    # A method called greet_user() prints a personalized greeting
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

# Create instances representing different users
user1 = User("John", "Doe", 30, "john@example.com")
user2 = User("Alice", "Smith", 25, "alice@example.com")
user3 = User("Bob", "Johnson", 40, "bob@example.com")

# Call methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
