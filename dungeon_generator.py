# Description: This file contains the main function to generate a dungeon, which is composed of five rooms and four or five corridors. Each room has a random encounter and items assigned to it. The dungeon is then displayed.

import json
import random
from units.room import Room
from units.item import Item
from units.dungeon import Dungeon
from units.corridor import Corridor
from units.encounter import Encounter

def load_rooms():
    with open('assets/rooms.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        rooms = [Room(**room) for room in data['rooms']]
    return rooms


def load_boss_rooms_from_json():
    with open('assets/rooms_boss.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        rooms = [Room(**room) for room in data['rooms']]
    return rooms

def load_reward_rooms_from_json():
    with open('assets/rooms_reward.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        rooms = [Room(**room) for room in data['rooms']]
    return rooms

def load_corridors_from_json():
    with open('assets/corridors.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        corridors = [Corridor(**corridor) for corridor in data['corridors']]
    return corridors

def load_encounters():
    with open('assets/encounters.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        encounters = [Encounter(**encounter) for encounter in data['encounters']]
    return encounters

def load_items():
    with open('assets/items.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        items = [Item(**item) for item in data['items']]
    return items


def generate_random_encounter_in_room(room, encounters, difficulty):
    if room.has_encounter:
        
        filtered_encounters = [enc for enc in encounters if enc.difficulty == difficulty]
        
        if filtered_encounters:
            encounter = random.choice(filtered_encounters)
            room.set_encounter(encounter)

def generate_encounters(rooms):
    encounters = load_encounters()
    generate_random_encounter_in_room(rooms[0], encounters, "Easy")
    generate_random_encounter_in_room(rooms[1], encounters, "Easy")
    generate_random_encounter_in_room(rooms[2], encounters, "Easy")
    generate_random_encounter_in_room(rooms[3], encounters, "Medium") # Boss room
    generate_random_encounter_in_room(rooms[4], encounters, "Easy")

def assign_random_item_to_room(room, items):
    random_item = random.choice(items)
    room.add_item(random_item)

def assign_items_to_rooms(rooms):
    items = load_items()
    
    common_items = [item for item in items if item.rarity == "Common"]
    uncommon_items = [item for item in items if item.rarity == "Uncommon"]
    rare_items = [item for item in items if item.rarity == "Rare"]

    for room in rooms:

        if room.is_reward:
            if room.common_items:
                num_common_items = random.randint(1, 2)
                for _ in range(num_common_items):
                    assign_random_item_to_room(room, common_items)

            if room.uncommon_items and random.random() <= 0.5:
                assign_random_item_to_room(room, uncommon_items)

            if room.rare_items and random.random() <= 0.2:
                assign_random_item_to_room(room, rare_items)

        else: 
            if room.common_items:
                num_common_items = random.randint(0, 2)
                for _ in range(num_common_items):
                    assign_random_item_to_room(room, common_items)

            if room.uncommon_items and random.random() <= 0.125:
                assign_random_item_to_room(room, uncommon_items)
                if random.random() <= 0.5:
                    assign_random_item_to_room(room, uncommon_items)

            if room.rare_items and random.random() <= 0.143:
                assign_random_item_to_room(room, rare_items)

def get_five_rooms():
    rooms = load_rooms()
    boss_rooms = load_boss_rooms_from_json()
    reward_rooms = load_reward_rooms_from_json()

    selected_rooms = random.sample(rooms, 3)
    selected_boss_room = random.choice(boss_rooms)
    selected_reward_room = random.choice(reward_rooms)

    remaining_reward_rooms = [room for room in reward_rooms if room != selected_reward_room]
    selected_secret_room = random.choice(remaining_reward_rooms)

    dungeon_rooms = selected_rooms + [selected_boss_room, selected_reward_room, selected_secret_room]

    return dungeon_rooms

def get_corridors():
    corridors = load_corridors_from_json()
    corridors_number = random.randint(4, 5)

    generated_corridors = random.choices(corridors, k=corridors_number)
    
    if corridors_number == 4:
        # Inserisce un corridoio con tutto False all'inizio
        empty_corridor = Corridor(ambush={}, trap={}, has_secret_door=False)
        generated_corridors.insert(0, empty_corridor)

    return generated_corridors

def generate_dungeon():
    rooms = get_five_rooms()
    corridors = get_corridors()

    generate_encounters(rooms)
    assign_items_to_rooms(rooms)

    dungeon = Dungeon(rooms,corridors)

    return dungeon

def main():
    dungeon = generate_dungeon()
    dungeon.display_dungeon()

if __name__ == "__main__":
    main()