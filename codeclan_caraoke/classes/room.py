class Room:

    name = str
    max_capacity = int
    playlist = []
    customers = []
    entry_fee = float
    till = float

    def __init__(self, name, max_capacity, playlist, customers, entry_fee, till):
        self.name = name
        self.max_capacity = max_capacity
        self.playlist = playlist
        self.customers = customers
        self.entry_fee = entry_fee
        self.till = till

    def add_customer_to_room(self, customer):
        self.customers.append(customer)

    def remove_customer_from_room(self, customer):
        self.customers.remove(customer)

    def add_new_song_to_playlist(self, song):
        self.playlist.append(song)
    
    def remove_song_from_playlist(self, song):
        self.playlist.remove(song)
    
    
