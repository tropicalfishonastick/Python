import random

# Initialize the list of aliens
aliens = []

def add_alien():
    aliens.append("Alien")

def remove_alien():
    if aliens:
        aliens.pop()

def game_loop():
    while True:
        action = input("Enter 'shoot' to shoot an alien, 'add' to add an alien, or 'quit' to exit: ").lower()
        
        if action == "shoot":
            remove_alien()
            print("Alien shot down!")
        elif action == "add":
            add_alien()
            print("New alien added!")
        elif action == "quit":
            print("Game over.")
            break
        else:
            print("Invalid action. Please enter 'shoot', 'add', or 'quit'.")

if __name__ == "__main__":
    print("Welcome to Alien Shooter!")
    add_alien()
    game_loop()
