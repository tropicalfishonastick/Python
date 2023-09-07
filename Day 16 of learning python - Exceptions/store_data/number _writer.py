'''write a short program that stores a set of numbers and another program
that reads these numbers back into memory. The first program will
use json.dumps() to store the set of numbers, and the second program will use
json.loads().
The json.dumps() function takes one argument: a piece of data that should
be converted to the JSON format. The function returns a string, which we can
then write to a data file'''

from pathlib import Path
import json # import the json module
numbers = [2, 3, 5, 7, 11, 13] # create a list of numbers to work with
path = Path('numbers.json') # choose a filename in which to store the list of numbers. It’s customary to use the file extension .json to indicate that the data in the file is stored in the JSON format
contents = json.dumps(numbers) # json.dumps() function to generate a string containing the JSON representation of the data
path.write_text(contents) # writing the data to the file using the same write_text() method