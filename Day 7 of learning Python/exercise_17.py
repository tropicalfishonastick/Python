'''Animals: Think of at least three different animals that have a common characteristic.
Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
• Modify your program to print a statement about each animal, such as A
dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in
common. You could print a sentence, such as Any of these animals would
make a great pet!'''

# List of animals with a common characteristic
animals = ["Dog", "Cat", "Rabbit"]

# Print animal names using a for loop
print("List of animals:")
for animal in animals:
    print(animal)

# Print statements about each animal
print("\nStatements about these animals:")
for animal in animals:
    print(f"A {animal.lower()} would make a great pet.")

# Print a concluding sentence about their common characteristic
print("\nAny of these animals would make a great pet!")
