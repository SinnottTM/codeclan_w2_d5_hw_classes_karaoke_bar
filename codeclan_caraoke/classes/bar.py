class Bar:

    name = str
    karaoke_rooms = []
    entry_price = float
    lobby = []
    total_guests = int

    def __init__(self, name, karaoke_rooms, entry_price, lobby, total_guests):
        self.name = name
        self.karaoke_rooms = karaoke_rooms
        self.entry_price = entry_price
        self.lobby = lobby
        self.total_guests = total_guests
