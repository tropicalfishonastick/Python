'''POSITIONAL ARGUMENT'''
# consider a function that displays information about pets. The function tells us what kind of animal each pet is and the pet’s name.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry') # positional argument
# Multiple Function Calls
# Describing a second, different pet requires just one more call to describe_pet():
describe_pet('dog', 'rio') # positional argument
describe_pet(animal_type='duck', pet_name='donald') # Keyword argument - 'name-value' pair : animal_type & pet_name is the key and duck & donald is the value