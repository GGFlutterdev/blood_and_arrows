import random
from difficulties import difficulties
import multiprocessing
from dungeon_generator import generate_dungeon

def average_damage_easy_dungeon_to_single_character(_=None):
    damage = 0
    dungeon = generate_dungeon(difficulty="Easy")
    for room in dungeon.rooms:
        encounter = room.encounter
        if encounter:
            if random.randint(1, 100) <= 60:
                damage += difficulties[encounter.difficulty]["DSP"]()
            else:
                damage += difficulties[encounter.difficulty]["DSN"]()
    for corridor in dungeon.corridors:
        if corridor.ambush and corridor.ambush.get("damage"):
            damage += corridor.ambush["damage"]
        if corridor.trap and corridor.trap.get("damage"):
            damage += corridor.trap["damage"]
    return damage

def calculate_average_damage_in_easy_dungeon(num_iterations):
    with multiprocessing.Pool(processes=6) as pool:
        results = pool.map(average_damage_easy_dungeon_to_single_character, range(num_iterations))

    average_damage = sum(results) / len(results)
    return average_damage