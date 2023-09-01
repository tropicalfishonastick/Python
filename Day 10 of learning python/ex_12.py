'''Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs
from this chapter, and extend it by adding new keys and values, changing
the context of the program, or improving the formatting of the output'''

# Extended Favorite Places Dictionary
favorite_places = {
    'Alice': ['Paris', 'London', 'New York'],
    'Bob': ['Tokyo', 'Sydney'],
    'Carol': ['Rome', 'Amsterdam', 'San Francisco'],
    'David': ['Rio de Janeiro', 'Berlin'],
    'Eve': ['Barcelona', 'Dubai', 'Cape Town']
}

# Improved Output Formatting
for person, places in favorite_places.items():
    print(f"{person}'s Favorite Places:")
    for i, place in enumerate(places, 1):  # Use enumerate to add numbering
        print(f"{i}. {place}")  # Display a numbered list of favorite places
    print("\n")
