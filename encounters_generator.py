import json
import random
from units.encounter import Encounter

def load_encounters():
    with open('assets/encounters.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        encounters = [Encounter(**encounter) for encounter in data['encounters']]
    return encounters


def generate_random_encounter_in_room(room, encounters, difficulty):
    if room.has_encounter:
        filtered_encounters = [enc for enc in encounters if enc.difficulty == difficulty]
        if filtered_encounters:
            encounter = random.choice(filtered_encounters)
            room.set_encounter(encounter)

def generate_encounters(rooms, difficulty):
    encounters = load_encounters()
    if difficulty == "Easy":
        generate_random_encounter_in_room(rooms[0], encounters, "Easy")
        generate_random_encounter_in_room(rooms[1], encounters, "Easy")
        generate_random_encounter_in_room(rooms[2], encounters, "Easy")
        generate_random_encounter_in_room(rooms[3], encounters, "Medium") # Boss room
        generate_random_encounter_in_room(rooms[4], encounters, "Easy")
    elif difficulty == "Medium":
        generate_random_encounter_in_room(rooms[0], encounters, "Medium")
        generate_random_encounter_in_room(rooms[1], encounters, "Medium")
        generate_random_encounter_in_room(rooms[2], encounters, "Medium")
        generate_random_encounter_in_room(rooms[3], encounters, "Hard") # Boss room
        generate_random_encounter_in_room(rooms[4], encounters, "Medium")
    elif difficulty == "Hard":
        generate_random_encounter_in_room(rooms[0], encounters, "Hard")
        generate_random_encounter_in_room(rooms[1], encounters, "Hard")
        generate_random_encounter_in_room(rooms[2], encounters, "Hard")
        generate_random_encounter_in_room(rooms[3], encounters, "Nightmare") # Boss room
        generate_random_encounter_in_room(rooms[4], encounters, "Hard")
    
