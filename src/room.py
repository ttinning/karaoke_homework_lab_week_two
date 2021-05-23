class Room:
    def __init__(self, room_name, room_list, song_list, room_capacity):
        self.room_name = room_name
        self.room_list = room_list
        self.song_list = song_list
        self.room_capacity = room_capacity
        self.room_till = 100
        
    def add_song(self, song):
        self.song_list.append(song)
        return self.song_list

    def add_person_to_room(self, guest):
        if len(self.room_list) < self.room_capacity:
            self.room_list.append(guest)    
            return self.room_list
        

    def remove_person_from_room(self, guest):
        self.room_list.remove(guest)
        return self.room_list

    def add_money_to_till(self, amount):
        self.room_till += amount
        return self.room_till

    def make_transaction(self, guest, price):
        guest.remove_cash(price)
        self.add_money_to_till(price)
