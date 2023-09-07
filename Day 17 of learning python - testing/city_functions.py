'''City, Country: Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country, such as Santiago, Chile. Store the function in a module called
city_functions.py, and save this file in a new folder so pytest won’t try to run the
tests we’ve already written.
Create a file called test_cities.py that tests the function you just wrote.
Write a function called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run the
test, and make sure test_city_country() passes.'''
# Create a Module city_functions.py: Create a new Python module named city_functions.py in a separate folder. 
# In this module, define a function format_city_country that accepts two parameters, city_name and country_name, 
# and returns a string in the format "City, Country."
# city_functions.py
def format_city_country(city_name, country_name):
    formatted_string = f"{city_name.title()}, {country_name.title()}"
    return formatted_string

'''Modify the city_functions.py Module:Update the format_city_country function in the city_functions.py module to accept a third, optional parameter for population. 
The function will return a formatted string with the population if provided and in the format "City, Country – population xxx".'''
# city_functions.py
def format_city_country(city_name, country_name, population=None):
    formatted_string = f"{city_name.title()}, {country_name.title()}"
    if population is not None:
        formatted_string += f" - population {population}"
    return formatted_string
