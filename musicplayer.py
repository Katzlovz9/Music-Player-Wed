from album import Album

class MusicPlayer:  
  def play(self, albums):
   for album in albums: 
    for song in album.songs:
      print(f"Playing {song.name}")
