'''Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.'''

# Create a dictionary to store information about three cities
cities = {
    'New York': {
        'country': 'USA',
        'population': '8.4 million',
        'fact': 'The Statue of Liberty is located here.'
    },
    'Paris': {
        'country': 'France',
        'population': '2.2 million',
        'fact': 'Known as the "City of Love."'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '13.5 million',
        'fact': 'Hosted the 2020 Summer Olympics.'
    }
}

# Loop through the dictionary and print information about each city
for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print("\n")
