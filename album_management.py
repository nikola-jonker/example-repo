''' 
Manages two lists of albums, demonstrating sorting, swapping,
copying, and searching.
'''

class Album: # Represents an album with a name, artist, and number of songs
    def __init__(self, album_name, album_artist, number_of_songs):
        '''
        Initialises an Album object.
        
        Args:
            album_name (str): The name of the album.
            album_artist (str): The artist of the album.
            number_of_songs (int): The number of songs in the album.
        '''
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs

    def __str__(self): # Returns a readable string representation of the album.
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

# Create albums1 with five albums
albums1 = [
    Album("Abbey Road", "The Beatles", 17),
    Album("The Dark Side of the Moon", "Pink Floyd", 10),
    Album("Back in Black", "AC/DC", 10),
    Album("Rumours", "Fleetwood Mac", 11),
    Album("Thriller", "Michael Jackson", 9)
]

for album in albums1:
    print(album)

# Sort albums1 by the number of songs in ascending order
albums1.sort(key=lambda album: album.number_of_songs)

print("\nAlbums sorted by number of songs:")
for album in albums1:
    print(album)

# Swap the first two albums in albums1
albums1[0], albums1[1] = albums1[1], albums1[0]

print("\nAlbums after swapping the first two:")
for album in albums1:
    print(album)

# Create albums2 with five different albums
albums2 = [
    Album("Hotel California", "Eagles", 9),
    Album("Led Zeppelin IV", "Led Zeppelin", 8),
    Album("Nevermind", "Nirvana", 12),
    Album("Born to Run", "Bruce Springsteen", 8),
    Album("The Wall", "Pink Floyd", 26)
]

print("\nAlbums in albums2:")
for album in albums2:
    print(album)

# Copy all albums from albums1 to albums2
albums2.extend(albums1)

# Add two more named albums to albums2
albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

# Sort albums2 alphabetically by album name
albums2.sort(key=lambda album: album.album_name)

print("\nAlbums in albums2 sorted by album name:")
for album in albums2:
    print(album)

# Search for "Dark Side of the Moon" and print its index
for index, album in enumerate(albums2):
    if album.album_name == "Dark Side of the Moon":
        print(f"\n'Dark Side of the Moon' found at index: {index}")
        break