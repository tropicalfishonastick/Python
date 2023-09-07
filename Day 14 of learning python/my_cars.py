from electric_car import Car, ElectricCar
my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())


# to import the entire car module and then create a regular car and an electric car:
import electric_car
my_mustang = electric_car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = electric_car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())