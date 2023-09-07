# write a separate program that uses json.loads() to read the list back into memory
from pathlib import Path
import json
path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents) # json.loads() function takes in a JSON-formatted string and returns a Python object (in this case, a list), which we assign to numbers
print(numbers)