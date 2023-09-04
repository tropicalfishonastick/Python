'''Restaurant: Make a class called Restaurant. 
The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods. 
Three Restaurants: Start with your class,
Create three different instances from the class, and call describe_restaurant() for each instance'''
class Restaurant:
    # The __init__() method initializes the restaurant_name and cuisine_type attributes
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # A method called describe_restaurant() prints restaurant information
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    # A method called open_restaurant() indicates that the restaurant is open
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")

# Create an instance of the Restaurant class
restaurant = Restaurant("My Restaurant", "Italian")

# Print the restaurant attributes individually
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

# Call the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
