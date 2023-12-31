# Working with Classes and Instances

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
      """Initialize attributes to describe a car."""
      self.make = make
      self.model = model
      self.year = year

    def get_descriptive_name(self):
       """Return a neatly formatted descriptive name."""
       long_name = f"{self.year} {self.make} {self.model}"
       return long_name.title()
    
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# Setting a Default Value for an Attribute
class Car:
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

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# Modifying an Attribute’s Value Directly
my_new_car.odometer_reading = 23 #******
my_new_car.read_odometer()


# Modifying an Attribute’s Value Through a Method
'''addition of update_odometer(). This
method takes in a mileage value and assigns it to self.odometer_reading.
Using the my_new_car instance, call update_odometer() with 23 as an argument
. This sets the odometer reading to 23, and read_odometer() prints
the reading:'''

class Car:
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

   def update_odometer(self, mileage): #*******
      """Set the odometer reading to the given value."""
      self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23) #*******
my_new_car.read_odometer()

'''extend the method update_odometer() to do additional work every
time the odometer reading is modified. add a little logic to make sure
no one tries to roll back the odometer reading:'''
class Car:
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

   def update_odometer(self, mileage): #*******
      """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
      """
      if mileage >= self.odometer_reading: # If the value provided for mileage is greater than
# or equal to the existing mileage, self.odometer_reading, update
# the odometer reading to the new mileage . If the new mileage is less
# than the existing mileage, you’ll get a warning that you can’t roll back an
# odometer
        self.odometer_reading = mileage
      else:
        print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23) #*******
my_new_car.read_odometer()


# Incrementing an Attribute’s Value Through a Method
'''Say we buy a used car and put 100 miles on it between the time we buy it and the time we register it. 
Here’s a method that allows us to pass this incremental amount and add that value
to the odometer reading'''

class Car:
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

    def update_odometer(self, mileage): #*******
        """Set the odometer reading to the given value.
            Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles): # new method increment_odometer() takes in a number of miles, and adds this value to self.odometer_reading.
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2019) # create a used car, my_used_car
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500) # set odometer to 23,500 by calling update_odometer() and passing 23_500
my_used_car.read_odometer()

my_used_car.increment_odometer(100) # call increment_odometer() and pass it 100 to add the 100 miles that we drove between buying the car and registering it
my_used_car.read_odometer()