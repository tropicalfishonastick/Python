'''City, Country: Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country, such as Santiago, Chile. Store the function in a module called
city_functions.py, and save this file in a new folder so pytest won’t try to run the
tests we’ve already written.
Create a file called test_cities.py that tests the function you just wrote.
Write a function called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run the
test, and make sure test_city_country() passes.'''


# Create a Test File test_cities.py:In the same folder where you have your city_functions.py, 
# create a test file named test_cities.py to test the format_city_country function.
# test_cities.py
from city_functions import format_city_country

def test_city_country():
    formatted_result = format_city_country('santiago', 'chile')
    assert formatted_result == 'Santiago, Chile'

'''Modify the test_cities.py Test File:Update the test_cities.py test file to test the modified format_city_country function. 
First, modify the existing test test_city_country to ensure it fails when the population is not provided.'''
# test_cities.py
from city_functions import format_city_country

def test_city_country():
    formatted_result = format_city_country('santiago', 'chile')
    assert formatted_result == 'Santiago, Chile'

'''Write a New Test test_city_country_population:Create a new test function called test_city_country_population to verify 
that you can call the function with the population parameter, and it returns the expected result.'''
# test_cities.py
def test_city_country_population():
    formatted_result = format_city_country('santiago', 'chile', population=5000000)
    assert formatted_result == 'Santiago, Chile - population 5000000'
