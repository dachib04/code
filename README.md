# code
#Getting the song's lyrics



import lyricsgenius

# Set your Genius API access token
access_token = "Your token"

# Create a Genius API client
genius = lyricsgenius.Genius(access_token)

# Search for the specified song
song_title = "Song's name"
artist_name = " singer "
song = genius.search_song(song_title, artist_name)

# Print the song's lyrics
print(song.lyrics)
