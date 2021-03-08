class Guest:

    name = str
    wallet = float
    favourite_song_artist_name = str
    favourite_song_artist_song = str

    def __init__(self, name, wallet, favourite_song_artist_song, favourite_song_artist_name):
        self.name = name
        self.wallet = wallet
        self.favourite_song_artist_song = favourite_song_artist_song
        self.favourite_song_artist_name = favourite_song_artist_name
