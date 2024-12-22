from units.room import Room
from units.corridor import Corridor

class Dungeon:
    def __init__(self, rooms: list[Room] = None, corridors: list[Corridor] = None):
        self.rooms = rooms if rooms is not None else []
        self.corridors = corridors if corridors is not None else []
    
    def display_dungeon(self):
        print("Dungeon Layout:\n")
        
        # Assumendo che l'ordine logico sia stanza-corridoio-stanza-corridoio...
        max_length = max(len(self.rooms), len(self.corridors))
        
        for i in range(max_length):
            if i < len(self.corridors):
                print(f" + Corridor {i + 1}: {self.corridors[i]}\n")
            if i < len(self.rooms):
                print(f" + Room {i + 1}: {self.rooms[i]}\n")
    
    def get_rooms(self):
        return self.rooms

    def get_corridors(self):
        return self.corridors
