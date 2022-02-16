from musicplayer import MusicPlayer
from album import Album

def main():
  player = MusicPlayer()

  albums = []

  num_albums = input("How many albums?")
  for i in range(int(num_albums)):
    name = input("Album Name? ")
    year = input("Album Year? ")

    artist = CreateArtist()
    songs = CreateSongs()
    album = Album(artist, songs, name, year)
    albums.append(album)

  player.play(albums)
  
def CreateArtist():
  name = input("Album Name? ")
  age = input("Album Age? ")
  artist = Artist(name, age)
  return artist

def CreateSongs():
  songs = []

  num_songs = input("How many songs? ")
  for i in range(int(num_songs)):
    name = input("Song name? ")
    duration = input("Song duration? ")
    song = Song(name, duration)
    songs.append(song)

  return songs

main()