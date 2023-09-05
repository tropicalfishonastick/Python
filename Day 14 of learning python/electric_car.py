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