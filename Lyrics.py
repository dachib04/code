

import lyricsgenius

# Set your Genius API access token
access_token = "9CZ4TgapsOxiwjI3NG94nAI3HPs__AxOtfZpHT8lKOjxkXDyH0rDtwpvQwXop0UFmoTZOxsgo2TTgpABWjaTAA"

# Create a Genius API client
genius = lyricsgenius.Genius(access_token)

# Search for the specified song
song_title = input("Song name: ")
artist_name = input(" singer: ")
song = genius.search_song(song_title, artist_name)

# Print the song's lyrics
print(song.lyrics)

