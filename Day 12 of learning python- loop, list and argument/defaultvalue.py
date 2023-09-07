'''Default Values'''
# set the default value of animal_type to 'dog'. Now anyone calling describe_pet() for a dog can omit that information:
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')

# simplest way to use this function now is to provide just a dog’s name in the function call:
describe_pet('willie')