import random
import concurrent.futures
from multiprocessing import Pool
from units.character import Character
from units.difficulties import difficulties
from dungeon_generator import generate_dungeon

def simulate_combat_iteration(args):
    team, difficulty = args
    dsp_func = difficulties[difficulty]["DSP"]
    dsn_func = difficulties[difficulty]["DSN"]
    results = {"all_alive": 0, "at_least_one_alive": 0, "all_dead": 0}
    team_hp = {f"{char.name}{i}": char.hp for i, char in enumerate(team)}

    for _ in range(3):
        combat_success = random.random() <= sum(c.combat_success_rate for c in team)
        for i, char in enumerate(team):
            char_name = f"{char.name}{i}"
            if combat_success:
                team_hp[char_name] -= dsp_func()
            else:
                team_hp[char_name] -= dsn_func()

    alive_count = sum(1 for hp in team_hp.values() if hp > 0)
    if alive_count == len(team):
        results["all_alive"] += 1
    elif alive_count > 0:
        results["at_least_one_alive"] += 1
    else:
        results["all_dead"] += 1

    remaining_hp = {char_name: max(0, hp) for char_name, hp in team_hp.items()}
    print(remaining_hp)

    return results

# Combina i risultati
def combine_iteration_results(batch_results):
    combined = {"all_alive": 0, "at_least_one_alive": 0, "all_dead": 0}
    for result in batch_results:
        for key in combined:
            combined[key] += result[key]
    return combined

def plot_results(results, team_name):
    labels = ["Tutti Salvi", "AlmeFalse UFalse Salvo", "Tutti Morti"]
    values = [results["all_alive"], results["at_least_one_alive"], results["all_dead"]]
    plt.bar(labels, values, color=["green", "orange", "red"])
    plt.title(f"Risultati dei Combattimenti - {team_name}")
    plt.ylabel("Numero di Prove")
    plt.xlabel("Risultati")
    plt.show()


# Simula in parallelo
def parallel_simulate_combats():
    teams = {
        #"Team Completo": [classes["Fighter"], classes["Mage"], classes["Healer"], classes["Explorer"]],
        "Team Completo 2": [classes["Berserker"], classes["Mage"], classes["Healer"], classes["Explorer"]],
        "Solo Combattenti": [classes["Fighter"]] * 4,
        "Solo Guaritori": [classes["Healer"]] * 4,
        "Solo Maghi": [classes["Mage"]] * 4,
    }
    num_iterations = 1000000
    difficulty = "Easy"
    for team_name, team in teams.items():
        args = [(team, difficulty) for _ in range(num_iterations)]
        with Pool() as pool:
            batch_results = pool.map(simulate_combat_iteration, args)
        results = combine_iteration_results(batch_results)
        print(f"{team_name}: {results}")
        plot_results(results, team_name)

def number_of_dungeons_to_get_full_equip(_=None):
    leather_armors = 0
    rings = 0
    number_of_dungeons = 0
    while leather_armors < 4 and rings < 8:
        dungeon = generate_dungeon()
        rooms = dungeon.rooms
        for room in rooms:
            items = room.items
            for item in items:
                if item.name == "Leather armor":
                    leather_armors += 1
                if item.name == "Precious Ring":
                    rings += 1
        number_of_dungeons += 1
    return number_of_dungeons

def calculate_average_number_of_dungeons_to_get_full_equip():
    num_iterations = 50000
    
    with concurrent.futures.ProcessPoolExecutor(6) as executor:
        results = list(executor.map(number_of_dungeons_to_get_full_equip, range(num_iterations)))

    average = sum(results) / len(results)
    return average

def number_of_dungeons_to_get_the_rares(_=None):
    amulets = 0
    magic_staffs = 0
    number_of_dungeons = 0

    while not (amulets >= 1 and magic_staffs >= 1):
        dungeon = generate_dungeon()
        rooms = dungeon.rooms
        for room in rooms:
            items = room.items
            for item in items:
                if item.name == "Goblin Slayer's Amulet" and amulets < 1:
                    amulets += 1
                if item.name == "Magic Staff" and magic_staffs < 1:
                    magic_staffs += 1

        number_of_dungeons += 1

    return number_of_dungeons

def calculate_average_number_of_dungeons_to_get_the_rares():
    num_iterations = 50000
    
    with concurrent.futures.ProcessPoolExecutor(6) as executor:
        results = list(executor.map(number_of_dungeons_to_get_the_rares, range(num_iterations)))

    average = sum(results) / len(results)
    return average

def number_of_dungeons_to_get_the_first_rare(_=None):
    rares = 0
    number_of_dungeons = 0
    while rares < 1:
        dungeon = generate_dungeon()
        rooms = dungeon.rooms
        for room in rooms:
            items = room.items
            for item in items:
                if item.rarity == "Rare":
                    rares += 1
        number_of_dungeons += 1
    return number_of_dungeons

def calculate_average_number_of_dungeons_to_get_the_first_rare():
    num_iterations = 50000
    
    with concurrent.futures.ProcessPoolExecutor(6) as executor:
        results = list(executor.map(number_of_dungeons_to_get_the_first_rare, range(num_iterations)))

    average = sum(results) / len(results)
    return average

def main():
    
    average_full_equip = calculate_average_number_of_dungeons_to_get_full_equip()
    print(f"Numero medio di dungeon per ottenere l'equipaggiamento completo: {average_full_equip}")
    
    average_rares = calculate_average_number_of_dungeons_to_get_the_rares()
    print(f"Numero medio di dungeon per ottenere entrambe le rare: {average_rares}")
    
    average_first_rare = calculate_average_number_of_dungeons_to_get_the_first_rare()
    print(f"Numero medio di dungeon per ottenere la prima rara: {average_first_rare}")

if __name__ == "__main__":
    main()