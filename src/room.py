class Room:
    def __init__(self, name, guest_list, song_list):
        self.name = name
        self.guest_list = guest_list
        self.song_list = song_list
        
    def add_song(self, song):
        self.song_list.append(song)
        return self.song_list

    def add_person_to_room(self, guest):
        self.guest_list.append(guest)
        return self.guest_list
