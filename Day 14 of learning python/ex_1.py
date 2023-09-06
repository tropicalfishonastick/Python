'''Number Served: Start with your program . Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, and then change this value and print it again.'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Initialize the restaurant with a name and cuisine type
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # Initialize the number of customers served to 0
        self.number_served = 0

    def describe_restaurant(self):
        # Print information about the restaurant
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        # Print a message indicating that the restaurant is open
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, num_customers):
        # Set the number of customers served
        self.number_served = num_customers

    def increment_number_served(self, additional_customers):
        # Increment the number of customers served by a given amount
        self.number_served += additional_customers

# Create an instance of the Restaurant class called 'restaurant'
restaurant = Restaurant("The Great Feast", "Italian")

# Print the initial number of customers served (0)
print(f"Number of customers served: {restaurant.number_served}")

# Change the number of customers served using the set_number_served method
restaurant.set_number_served(50)

# Print the updated number of customers served (50)
print(f"Updated number of customers served: {restaurant.number_served}")

# Increment the number of customers served by 10
restaurant.increment_number_served(10)

# Print the incremented number of customers served (60)
print(f"Incremented number of customers served: {restaurant.number_served}")



'''Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class. Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.'''

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        # Call the constructor of the parent class (Restaurant)
        super().__init__(restaurant_name, cuisine_type="Ice Cream")
        self.flavors = flavors

    def display_flavors(self):
        # Print the available ice cream flavors
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Create an instance of the IceCreamStand class
ice_cream_stand = IceCreamStand("Sweet Treats", ["Vanilla", "Chocolate", "Strawberry", "Mint Chip"])

# Call the display_flavors method to display the ice cream flavors
ice_cream_stand.display_flavors()




