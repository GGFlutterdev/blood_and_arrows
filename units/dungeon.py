from units.room import Room
from units.corridor import Corridor

class Dungeon:
    def __init__(self, rooms: list[Room] = None, corridors: list[Corridor] = None):
        self.rooms = rooms if rooms is not None else []
        self.corridors = corridors if corridors is not None else []
    
    def display_dungeon(self):
        print("Dungeon Rooms:")
        for room in self.rooms:
            print(' + ' + str(room))

        print("\nDungeon Corridors:")
        for corridor in self.corridors:
            print(' + ' + str(corridor))

    def get_rooms(self):
        return self.rooms

    def get_corridors(self):
        return self.corridors