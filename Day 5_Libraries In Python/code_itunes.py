import requests     # Import the requests module to make HTTP requests
import sys         # Import the sys module to access command-line arguments

if len(sys.argv) != 2:
    sys.exit()     # Exit the script if there are not exactly two command-line arguments

# Construct the URL for the iTunes Search API by appending the search term from command-line argument
url = "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]

# Make an HTTP GET request to the constructed URL
response = requests.get(url)

# Print the JSON response from the API, which contains information about the song
print(response.json())

import json         # Import the json module to work with JSON data
import requests     # Import the requests module to make HTTP requests
import sys         # Import the sys module to access command-line arguments

if len(sys.argv) != 2:
    sys.exit()     # Exit the script if there are not exactly two command-line arguments

# Construct the URL for the iTunes Search API by appending the search term from command-line argument
url = "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]

# Make an HTTP GET request to the constructed URL
response = requests.get(url)

# Convert the JSON response to a nicely formatted string with indentation
formatted_json = json.dumps(response.json(), indent=2)

# Print the formatted JSON string
print(formatted_json)

import json         # Import the json module to work with JSON data
import requests     # Import the requests module to make HTTP requests
import sys         # Import the sys module to access command-line arguments

if len(sys.argv) != 2:
    sys.exit()     # Exit the script if there are not exactly two command-line arguments

# Construct the URL for the iTunes Search API by appending the search term from command-line argument
url = "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]

# Make an HTTP GET request to the constructed URL
response = requests.get(url)

# Convert the JSON response to a Python dictionary using response.json()
response_data = response.json()

# Iterate over the "results" list within the response data
for result in response_data["results"]:
    # Print the "trackName" attribute from each result
    print(result["trackName"])
