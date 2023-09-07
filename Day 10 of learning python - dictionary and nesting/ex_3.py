'''Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.'''

# Create a dictionary to store programming terms and their meanings
glossary = {
    'variable': 'A storage location in a program that holds data.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'loop': 'A control structure used to repeatedly execute a block of code.',
    'list': 'A data structure that stores a collection of items in a specific order.',
    'dictionary': 'A data structure that stores key-value pairs.'
}

# Print each word and its meaning with a newline between each pair
for word, meaning in glossary.items():
    print(f"{word}:")
    print(meaning + "\n")
