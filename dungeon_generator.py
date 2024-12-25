# Description: This file contains the main function to generate a dungeon, which is composed of five rooms and five corridors.
# Each room has a random encounter, items and chest assigned to it.
# Each corridor has a random ambush, trap or secret door.
# The dungeon is then displayed.

import json
import random
from units.room import Room
from units.dungeon import Dungeon
from units.corridor import Corridor
from items_generator import assign_items_to_rooms
from encounters_generator import generate_encounters

def load_rooms():
    with open('assets/rooms.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        rooms = [Room(**room) for room in data['rooms']]
    return rooms

def load_corridors_from_json():
    with open('assets/corridors.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        corridors = [Corridor(**corridor) for corridor in data['corridors']]
    return corridors

def get_five_rooms():
    all_rooms = load_rooms()
    boss_rooms = [room for room in all_rooms if room.is_boss]
    reward_rooms = [room for room in all_rooms if room.is_reward]
    rooms = [room for room in all_rooms if not room.is_boss and not room.is_reward]

    selected_rooms = random.sample(rooms, 3)
    selected_boss_room = random.choice(boss_rooms)
    selected_reward_room = random.choice(reward_rooms)

    remaining_reward_rooms = [room for room in reward_rooms if room != selected_reward_room]
    selected_secret_room = random.choice(remaining_reward_rooms)

    dungeon_rooms = selected_rooms + [selected_boss_room, selected_reward_room, selected_secret_room]

    assign_items_to_rooms(dungeon_rooms)

    return dungeon_rooms

def get_corridors():
    corridors = load_corridors_from_json()
    corridors_number = 5

    generated_corridors = random.choices(corridors, k=corridors_number)
    return generated_corridors

def generate_dungeon(difficulty):
    rooms = get_five_rooms()
    corridors = get_corridors()

    generate_encounters(rooms, difficulty)
    
    dungeon = Dungeon(rooms,corridors)

    return dungeon

def main():
    dungeon = generate_dungeon(difficulty="Easy")
    dungeon.display_dungeon()

if __name__ == "__main__":
    main()