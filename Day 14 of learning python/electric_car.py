class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

'''We start with Car 1. When you create a child class, the parent class must be part of the current file and must appear before the child class in the file. 
We then define the child class, ElectricCar 2. The name of the parent class must be included in parentheses in the definition of a child class. 
The __init__() method takes in the information required to make a Car instance 3.
The super() function 4 is a special function that allows you to call a method from the parent class. 
This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method. 
The name super comes from a convention of calling the parent class a superclass and the child class a subclass.
We test whether inheritance is working properly by trying to create an electric car with the same kind of information we’d provide when making a regular car. 
We make an instance of the ElectricCar class and assign it to my_leaf 5. This line calls the __init__() method defined in ElectricCar, which in turn tells Python to call the __init__() method defined in the parent class Car. 
We provide the arguments 'nissan', 'leaf', and 2024. Aside from __init__(), there are no attributes or methods yet that are
particular to an electric car. At this point we’re just making sure the electric
car has the appropriate Car behaviors. The ElectricCar instance works just like an instance of Car, so now we
can begin defining attributes and methods specific to electric cars.'''



# Defining Attributes and Methods for the Child Class
''''Once you have a child class that inherits from a parent class, you can add
any new attributes and methods necessary to differentiate the child class
from the parent class.
Let’s add an attribute that’s specific to electric cars (a battery, for example)
and a method to report on this attribute. We’ll store the battery size and
write a method that prints a description of the battery:'''
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery_size = 40 # add a new attribute self.battery_size and set its initial value to 40. This attribute will be associated with all instances created from the ElectricCar class but won’t be associated with any instances of Car

    def describe_battery(self): # add a method called describe_battery() that prints information about the battery. we call this method, we get a description that is clearly specific to an electric car
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()


# Instances as Attributes
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery: # define a new class called Battery that doesn’t inherit from any other class.
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40): # The __init__() method 1 has one parameter, battery_size, in addition to self. This is an optional parameter that sets the battery’s size to 40 if no value is provided
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self): # The method describe_battery() has been moved to this class as well
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    # add another method to Battery that reports the range of the car based on the battery size:
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
           range = 150
        elif self.battery_size == 65:
           range = 225

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery() # In the ElectricCar class, add an attribute called self.battery
                                 # This line tells Python to create a new instance of Battery (with a default size
                                 # of 40, because we’re not specifying a value) and assign that instance to the
                                 # attribute self.battery. This will happen every time the __init__() method
                                 # is called; any ElectricCar instance will now have a Battery instance created
                                 # automatically.
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery() # This line tells Python to look at the instance my_leaf, find its battery attribute, and call the method describe_battery() that’s associated with the Battery instance assigned to the attribute.
my_leaf.battery.get_range()