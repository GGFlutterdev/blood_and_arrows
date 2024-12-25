# Description: This script contains the main function that runs the simulation and calculates the average number of dungeons needed to get the full equipment and the first rare.
# It is essential to assign the right rarity to the items in the dungeon_generator.py, assign_items_to_rooms script. The simulation is run using the multiprocessing module to speed up the process.

import multiprocessing
from dungeon_generator import generate_dungeon

num_iterations = 10000

def number_of_dungeons_to_get_full_equip(_=None):
    amulets = 0
    rings = 0
    number_of_dungeons = 0
    while amulets < 4 and rings < 8:
        dungeon = generate_dungeon(difficulty="Easy")
        rooms = dungeon.rooms
        for room in rooms:
            items = room.items
            for item in items:
                if item.name == "Shiny Amulet":
                    amulets += 1
                if item.name == "Precious Ring":
                    rings += 1
        number_of_dungeons += 1
    return number_of_dungeons

def calculate_average_number_of_dungeons_to_get_full_equip():
    with multiprocessing.Pool(processes=6) as pool:
        results = pool.map(number_of_dungeons_to_get_full_equip, range(num_iterations))

    average = sum(results) / len(results)
    return average

def number_of_dungeons_to_get_the_first_rare(_=None):
    rares = 0
    number_of_dungeons = 0
    while rares < 1:
        dungeon = generate_dungeon(difficulty="Easy")
        rooms = dungeon.rooms
        for room in rooms:
            items = room.items
            for item in items:
                if item.rarity == "Rare":
                    rares += 1
        number_of_dungeons += 1
    return number_of_dungeons

def calculate_average_number_of_dungeons_to_get_the_first_rare():
    with multiprocessing.Pool(processes=6) as pool:
        results = pool.map(number_of_dungeons_to_get_the_first_rare, range(num_iterations))

    average = sum(results) / len(results)
    return average

def main():

    print("In circa 3 dungeon bisogna riuscire ad ottenere l'equipaggiamento completo.")
    print("In circa 4 dungeon bisogna riuscire ad ottenere la prima rara.")
    
    average_full_equip = calculate_average_number_of_dungeons_to_get_full_equip()
    print(f"Numero medio di dungeon per ottenere l'equipaggiamento completo: {average_full_equip}")
    
    average_first_rare = calculate_average_number_of_dungeons_to_get_the_first_rare()
    print(f"Numero medio di dungeon per ottenere la prima rara: {average_first_rare}")

if __name__ == "__main__":
    main()
