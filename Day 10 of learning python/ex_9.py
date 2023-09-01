'''Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places for
each person. To make this exercise a bit more interesting, ask some friends to
name a few of their favorite places. Loop through the dictionary, and print each
person’s name and their favorite places.'''

# Create a dictionary to store favorite places for different people
favorite_places = {
    'Alice': ['Paris', 'London', 'New York'],
    'Bob': ['Tokyo', 'Sydney'],
    'Carol': ['Rome']
}

# Loop through the dictionary and print each person's name and their favorite places
for person, places in favorite_places.items():
    print(f"{person}'s Favorite Places:")
    for place in places:
        print(f"- {place}")
    print("\n")
