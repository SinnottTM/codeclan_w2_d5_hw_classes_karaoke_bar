class Bar:

    name = str
    karaoke_rooms = []
    entry_price = int
    till = int
    bar_lobby = []
    total_guests = int
    drinks_list = []

    def __init__(self, name, karaoke_rooms, entry_price, till, bar_lobby, total_guests, drinks_list):
        self.name = name
        self.karaoke_rooms = karaoke_rooms
        self.entry_price = entry_price
        self.till = till
        self.bar_lobby = bar_lobby
        self.total_guests = total_guests
        self.drinks_list = drinks_list

    def add_guest_to_bar_lobby(self, guest):
        if guest.wallet > self.entry_price:
            self.till += self.entry_price
            guest.wallet -= self.entry_price
            self.bar_lobby.append(guest)
        else:
            return "No cash, no Karaoke"

    def create_new_karaoke_room(self, room):
        self.karaoke_rooms.append(room)

    def remove_karaoke_room(self, room):
        self.karaoke_rooms.remove(room)
    
    def send_guest_to_karaoke_room(self, customer, room, bar):
        room.add_guest_to_room(customer)
        # Caused error when run, removed but would like to review to find out where this issue was coming from
        # self.bar_lobby.remove(customer)

    def customer_beer_order(self, guest):
        print("Guinness is £5")
        if guest.wallet > 5:
           guest.wallet -= 5
           self.till += 5
           return "Enjoy"
        else:
            return "No Guinness for you, so sad"
            
    def total_guests_number(self, room):
        self.total_guests += (len(self.bar_lobby) + len(room.guests))
        return self.total_guests

    def add_drink_to_drink_list(self, drink):
        self.drinks_list.append(drink)

    def remove_drink_from_drink_list(self, drink):
        self.drinks_list.remove(drink)
