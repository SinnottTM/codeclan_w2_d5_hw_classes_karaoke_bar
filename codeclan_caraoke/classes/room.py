class Room:

    name = str
    max_capacity = int
    playlist = []
    guests = []

    def __init__(self, name, max_capacity, playlist, guests):
        self.name = name
        self.max_capacity = max_capacity
        self.playlist = playlist
        self.guests = guests

    def add_guest_to_room(self, guest):
        if self.max_capacity > len(self.guests):
            self.guests.append(guest)
        # else:
        #     bar.add_guest_to_bar_lobby(guest)
        #     # return "Room is too full, sorry"

    def remove_guest_from_room(self, guest, bar):
        bar.add_guest_to_bar_lobby(guest)
        self.guests.remove(guest)
    
    def add_new_song_to_playlist(self, song):
        self.playlist.append(song)
    
    def remove_song_from_playlist(self, song):
        self.playlist.remove(song)

    def check_favourite_song(self,guest):
        for song in self.playlist:
            if guest.favourite_song_artist_song == song.name:
                return "Oh I love this song!"
        else:
            return "This place sucks!"
