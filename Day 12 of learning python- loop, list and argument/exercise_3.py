'''City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values
that are returned.'''

def city_country(city, country):
    formatted_string = f"{city}, {country}"
    return formatted_string

# Calling the function with three city-country pairs
result1 = city_country("Santiago", "Chile")
result2 = city_country("Tokyo", "Japan")
result3 = city_country("Paris", "France")

# Printing the values returned by the function
print(result1)
print(result2)
print(result3)
