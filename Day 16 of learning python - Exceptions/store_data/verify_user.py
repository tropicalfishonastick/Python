'''Verify User: The final listing for remember_me.py assumes either that the user has already entered their username or 
that the program is running for the first time. We should modify it in case the current user is not the person who last used the program.
Before printing a welcome back message in greet_user(), ask the user if this is the correct username. 
If it’s not, call get_new_username() to get the correct username.'''
import json

def get_user_data():
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
        return user_data
    except FileNotFoundError:
        return None

def get_new_username():
    username = input("Enter your username: ")
    return username

def main():
    user_data = get_user_data()

    if user_data:
        # Verify the username
        stored_username = user_data.get('username')
        current_username = input(f"Is '{stored_username}' your username? (yes/no): ").strip().lower()

        if current_username == 'yes':
            print("Welcome back!")
            print("User Data:")
            for key, value in user_data.items():
                print(f"{key}: {value}")
        else:
            user_data['username'] = get_new_username()
            with open('user_data.json', 'w') as file:
                json.dump(user_data, file)
                print("Your username has been updated.")
    else:
        user_data = {}
        user_data['username'] = get_new_username()
        user_data['favorite_number'] = input("What is your favorite number? ")

        with open('user_data.json', 'w') as file:
            json.dump(user_data, file)
            print("Your user data has been saved.")

if __name__ == '__main__':
    main()
