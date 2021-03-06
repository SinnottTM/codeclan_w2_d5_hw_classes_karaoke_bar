class Guest:

    name = str
    wallet = float
    favourite_song = str

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    # def whatever(self):
    #   some_logic
    #   return bleh
