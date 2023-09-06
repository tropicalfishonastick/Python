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



'''Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class. Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described above.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.'''

# Define the User class as you provided it

# Define the Privileges class to store a list of privileges
class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Define the Admin class that inherits from the User class
class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        # Create an instance of Privileges as an attribute in Admin
        self.privileges = Privileges()

# Create an instance of Admin
admin_user = Admin("Admin", "User", 35, "admin@example.com")

# Add privileges to the admin_user's Privileges instance
admin_user.privileges.privileges = ["can add post", "can delete post", "can ban user"]

# Call the show_privileges method to display the admin_user's privileges
admin_user.privileges.show_privileges()
