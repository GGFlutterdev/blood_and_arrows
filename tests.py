from drop_simulation import calculate_average_number_of_dungeons_to_get_the_first_rare
from drop_simulation import calculate_average_number_of_dungeons_to_get_full_equip
from combat_simulation import calculate_average_damage_in_easy_dungeon

def main():
    print("🧪 Running tests...")
    average_number_of_dungeons_to_get_the_first_rare = calculate_average_number_of_dungeons_to_get_the_first_rare()
    average_number_of_dungeons_to_get_full_equip = calculate_average_number_of_dungeons_to_get_full_equip()
    average_damage_in_easy_dungeon = calculate_average_damage_in_easy_dungeon()

    # Test sul numero di dungeon per il primo oggetto raro
    if average_number_of_dungeons_to_get_the_first_rare > 3.8 and average_number_of_dungeons_to_get_the_first_rare < 4.1:
        print(f"✅ Numero medio di dungeon per ottenere il primo oggetto raro: {average_number_of_dungeons_to_get_the_first_rare:.2f}")
    elif average_number_of_dungeons_to_get_the_first_rare < 2.7:
        print(f"⚠️ Il numero medio di dungeon per ottenere il primo oggetto raro è troppo basso! ({average_number_of_dungeons_to_get_the_first_rare:.2f}). Il valore ottimale è compreso tra 2.7 e 4.1.")
    elif average_number_of_dungeons_to_get_the_first_rare > 4.1:
        print(f"⚠️ Il numero medio di dungeon per ottenere il primo oggetto raro è troppo alto! ({average_number_of_dungeons_to_get_the_first_rare:.2f}). Il valore ottimale è compreso tra 2.7 e 4.1.")

    # Test sul numero di dungeon per il full equip
    if average_number_of_dungeons_to_get_full_equip > 2.7 and average_number_of_dungeons_to_get_full_equip < 3.0:
        print(f"✅ Numero medio di dungeon per ottenere il full equip per tutto il gruppo: {average_number_of_dungeons_to_get_full_equip:.2f}")
    elif average_number_of_dungeons_to_get_full_equip < 2.7:
        print(f"⚠️ Il numero medio di dungeon per ottenere il full equip è troppo basso! ({average_number_of_dungeons_to_get_full_equip:.2f}). Il valore ottimale è compreso tra 2.7 e 3.0.")
    elif average_number_of_dungeons_to_get_full_equip > 3.0:
        print(f"⚠️ Il numero medio di dungeon per ottenere il full equip è troppo alto! ({average_number_of_dungeons_to_get_full_equip:.2f}). Il valore ottimale è compreso tra 2.7 e 3.0.")

    # Test sul danno medio in un dungeon facile
    if average_damage_in_easy_dungeon > 21 and average_damage_in_easy_dungeon < 22:
        print(f"✅ Danno medio in un dungeon facile: {average_damage_in_easy_dungeon:.2f}")
    elif average_damage_in_easy_dungeon < 21:
        print(f"⚠️ Il danno medio in un dungeon facile è troppo basso! ({average_damage_in_easy_dungeon:.2f}). Il valore ottimale è compreso tra 21 e 22.")
    elif average_damage_in_easy_dungeon > 22:
        print(f"⚠️ Il danno medio in un dungeon facile è troppo alto! ({average_damage_in_easy_dungeon:.2f}). Il valore ottimale è compreso tra 21 e 22.")

if __name__ == "__main__":
    main()