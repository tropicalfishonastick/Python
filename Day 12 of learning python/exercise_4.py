'''Album: Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
Make at least one new function call that includes the number of songs on an album.'''

def make_album(artist, title, num_songs=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album

# Creating three different album dictionaries
album1 = make_album("Artist1", "Album Title 1")
album2 = make_album("Artist2", "Album Title 2", 12)
album3 = make_album("Artist3", "Album Title 3")

# Printing each album dictionary
print(album1)
print(album2)
print(album3)
