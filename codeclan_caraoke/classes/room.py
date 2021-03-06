class Room:

    name = str
    guests = []
    playlist = []

    def __init__(self, name, guests, playlist):
        self.name = name
        self.guests = guests
        self.playlist = playlist

    # def max_capacity(self):
    #     if len(self.guests) > 8:
    #         return "Nope!"
    
