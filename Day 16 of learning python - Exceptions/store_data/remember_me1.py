'''User Dictionary: The remember_me.py example only stores one piece of information, the username. 
Expand this example by asking for two more pieces of information about the user, then store all the information you collect in a dictionary. 
Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). 
Print a summary showing exactly what your program remembers about the user.'''
import json

def get_user_data():
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
        return user_data
    except FileNotFoundError:
        return None

def main():
    user_data = get_user_data()

    if user_data:
        print("Welcome back!")
        print("User Data:")
        for key, value in user_data.items():
            print(f"{key}: {value}")
    else:
        user_data = {}
        user_data['username'] = input("Enter your username: ")
        user_data['favorite_number'] = input("What is your favorite number? ")

        with open('user_data.json', 'w') as file:
            json.dump(user_data, file)
            print("Your user data has been saved.")

if __name__ == '__main__':
    main()
