from artist import Artist
from song import Song

class Album:
  def __init__(self):
    self.artist = Artist()
    self.songs = [
      Song()
    ]
    self.name = "Christmas Songs"
    self.year = 2022