'''User Albums: Start with your program from Exercise_4.
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.'''

def make_album(artist, title, num_songs=None):
    album = {
        'artist': artist,
        'title': title,
    }
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album

while True:
    print("\nEnter album information (enter 'q' to quit):")
    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break

    num_songs = input("Number of songs (optional, press Enter to skip): ")
    if num_songs == 'q':
        break
    elif num_songs:
        album_info = make_album(artist, title, int(num_songs))
    else:
        album_info = make_album(artist, title)

    print("\nAlbum information:")
    print(album_info)
