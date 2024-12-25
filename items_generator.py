import json
import random
from units.item import Item

def load_items():
    with open('assets/items.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        items = [Item(**item) for item in data['items']]
    return items

def assign_random_item_to_room(room, items, probability=1):
    if random.random() <= probability:
        random_item = random.choice(items)
        room.add_item(random_item)

def assign_items_to_rooms(rooms):
    items = load_items()
    
    common_items = [item for item in items if item.rarity == "Common"]
    uncommon_items = [item for item in items if item.rarity == "Uncommon"]
    rare_items = [item for item in items if item.rarity == "Rare"]

    for room in rooms:

        if room.is_reward or (room.chest != None and room.chest.type != "Mimic"):
            if room.common_items:
                num_common_items = random.randint(1, 2)
                for _ in range(num_common_items):
                    assign_random_item_to_room(room, common_items)

            if room.uncommon_items:
                assign_random_item_to_room(room, uncommon_items, 0.125)
                assign_random_item_to_room(room, uncommon_items, 0.1)

            if room.rare_items:
                assign_random_item_to_room(room, rare_items, 0.2)

        else: 
            if room.common_items:
                num_common_items = random.randint(0, 2)
                for _ in range(num_common_items):
                    assign_random_item_to_room(room, common_items)

            if room.uncommon_items:
                assign_random_item_to_room(room, uncommon_items, 0.167)

            if room.rare_items:
                assign_random_item_to_room(room, rare_items, 0.143)