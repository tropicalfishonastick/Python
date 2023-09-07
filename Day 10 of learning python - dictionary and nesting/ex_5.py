'''Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.'''

# Create a dictionary of major rivers and the countries they run through
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

# Use a loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Use a loop to print the name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river)

# Use a loop to print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
