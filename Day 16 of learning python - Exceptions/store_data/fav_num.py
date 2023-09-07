'''Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dumps() to store this number in a file. Write a separate program that reads in this value and prints the message “I know your favorite
number! It’s _____.”'''
import json

# Prompt the user for their favorite number
favorite_number = input("What is your favorite number? ")

# Store the favorite number in a JSON file
filename = 'favorite_number.json'
with open(filename, 'w') as file:
    json.dump(favorite_number, file)


'''Favorite Number Remembered: Combine the two programs into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works'''
import json

def get_favorite_number():
    try:
        with open('favorite_number.json', 'r') as file:
            favorite_number = json.load(file)
        return favorite_number
    except FileNotFoundError:
        return None

def main():
    favorite_number = get_favorite_number()
    
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        favorite_number = input("What is your favorite number? ")
        with open('favorite_number.json', 'w') as file:
            json.dump(favorite_number, file)
            print("Your favorite number has been saved.")

if __name__ == '__main__':
    main()
