# Import the 'random' module, which can be used later if needed
import random

# Initialize the list of aliens
aliens = []

# Function to add an alien to the list
def add_alien():
    aliens.append("Alien")

# Function to remove an alien from the list
def remove_alien():
    if aliens:
        aliens.pop()

# Function to manage the game loop
def game_loop():
    while True:
        # Get the player's action as input (lowercased for case-insensitivity)
        action = input("Enter 'shoot' to shoot an alien, 'add' to add an alien, or 'quit' to exit: ").lower()
        
        # Process the player's action
        if action == "shoot":
            remove_alien()  # Remove an alien from the list
            print("Alien shot down!")
        elif action == "add":
            add_alien()  # Add an alien to the list
            print("New alien added!")
        elif action == "quit":
            print("Game over.")  # Exit the game loop
            break
        else:
            print("Invalid action. Please enter 'shoot', 'add', or 'quit'.")

# Entry point of the program
if __name__ == "__main__":
    print("Welcome to Alien Shooter!")
    add_alien()  # Start with an initial alien
    game_loop()  # Start the game loop
#----------------------------------------------------------------------------------------------------------------------------------
#I've added comments to explain each section of the code:

#The code starts by importing the random module, although it's not used in the current version of the game.
#It initializes the aliens list to store the current aliens in the game.
#There are three functions: add_alien() to add an alien, remove_alien() to remove an alien, and game_loop() to manage the game loop.
#The game loop repeatedly asks the player for input and responds based on the entered action.
#If the action is "shoot," an alien is removed from the list.
#If the action is "add," a new alien is added to the list.
#If the action is "quit," the game loop ends.
#If the action is anything else, an invalid action message is displayed.
#The game loop starts after displaying a welcome message and adding an initial alien to the list.
#This basic structure provides the foundation for a simple text-based game where you can shoot aliens and add new ones to the list.