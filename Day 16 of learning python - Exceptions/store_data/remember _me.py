# compartmentalization of work

from pathlib import Path
import json
username = input("What is your name? ")
path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")


from pathlib import Path
import json

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    if path.exists(): # exists() method returns True if a file or folder exists and False if it doesn’t
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")
greet_user()


from pathlib import Path
import json

def get_stored_username(path): # retrieves a stored username and returns the username if it finds one. If the path that’s passed to get_stored_username() doesn’t exist, the function returns None
   """Get stored username if available."""
   if path.exists():
      contents = path.read_text()
      username = json.loads(contents)
      return username
   else:
      return None
   
def greet_user():
   """Greet the user by name."""
   path = Path('username.json')
   username = get_stored_username(path)
   if username:
      print(f"Welcome back, {username}!")
   else:
      username = input("What is your name? ")
      contents = json.dumps(username)
      path.write_text(contents)
      print(f"We'll remember you when you come back, {username}!")
greet_user()


from pathlib import Path
import json

def get_stored_username(path):
   """Get stored username if available."""
   if path.exists():
      contents = path.read_text()
      username = json.loads(contents)
      return username
   else:
      return None
   
def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
       print(f"Welcome back, {username}!")
    else:
       username = get_new_username(path)
       print(f"We'll remember you when you come back, {username}!")
greet_user()