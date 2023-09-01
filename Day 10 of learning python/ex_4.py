'''Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.'''

# Create a dictionary to store programming terms and their meanings
glossary = {
    'variable': 'A storage location in a program that holds data.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'loop': 'A control structure used to repeatedly execute a block of code.',
    'list': 'A data structure that stores a collection of items in a specific order.',
    'dictionary': 'A data structure that stores key-value pairs.'
}

# Function to print the glossary
def print_glossary(glossary):
    for word, meaning in glossary.items():
        print(f"{word}: {meaning}\n")

# Print the initial glossary
print("Initial Glossary:")
print_glossary(glossary)

# Add five more Python terms to the glossary
glossary['module'] = 'A file containing Python code that can be imported and reused.'
glossary['class'] = 'A blueprint for creating objects with shared properties and methods.'
glossary['inheritance'] = 'A mechanism in object-oriented programming that allows a class to inherit properties and methods from another class.'
glossary['exception'] = 'An error that occurs during program execution, which can be caught and handled.'
glossary['list comprehension'] = 'A concise way to create lists in Python by applying an expression to each item in an iterable.'

# Print the updated glossary
print("\nUpdated Glossary:")
print_glossary(glossary)
