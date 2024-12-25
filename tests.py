from drop_simulation import calculate_average_number_of_dungeons_to_get_full_equip
from drop_simulation import calculate_average_number_of_dungeons_to_get_the_first_rare
from combat_simulation import calculate_average_damage_to_single_chatacter_in_easy_dungeon
from combat_simulation import calculate_average_damage_to_single_chatacter_in_medium_dungeon
from drop_simulation import calculate_average_number_of_small_healing_potions_in_easy_dungeon


def main():
    num_iterations = 100000

    print("🧪 Running tests...")

    average_number_of_dungeons_to_get_full_equip = calculate_average_number_of_dungeons_to_get_full_equip(num_iterations)
    average_number_of_dungeons_to_get_the_first_rare = calculate_average_number_of_dungeons_to_get_the_first_rare(num_iterations)
    average_damage_to_single_chatacter_in_easy_dungeon = calculate_average_damage_to_single_chatacter_in_easy_dungeon(num_iterations)
    average_damage_to_single_chatacter_in_medium_dungeon = calculate_average_damage_to_single_chatacter_in_medium_dungeon(num_iterations)
    average_number_of_small_healing_potions_in_easy_dungeon = calculate_average_number_of_small_healing_potions_in_easy_dungeon(num_iterations)

    # Test sul numero di dungeon per il primo oggetto raro
    if average_number_of_dungeons_to_get_the_first_rare >= 3.8 and average_number_of_dungeons_to_get_the_first_rare <= 4.1:
        print(f"✅ Numero medio di dungeon per ottenere il primo oggetto raro: {average_number_of_dungeons_to_get_the_first_rare:.2f}")
    elif average_number_of_dungeons_to_get_the_first_rare < 3.8:
        print(f"⚠️ Il numero medio di dungeon per ottenere il primo oggetto raro è troppo basso! ({average_number_of_dungeons_to_get_the_first_rare:.2f}). Il valore ottimale è compreso tra 2.7 e 4.1.")
    elif average_number_of_dungeons_to_get_the_first_rare > 4.1:
        print(f"⚠️ Il numero medio di dungeon per ottenere il primo oggetto raro è troppo alto! ({average_number_of_dungeons_to_get_the_first_rare:.2f}). Il valore ottimale è compreso tra 2.7 e 4.1.")

    # Test sul numero di dungeon per il full equip
    if average_number_of_dungeons_to_get_full_equip >= 2.7 and average_number_of_dungeons_to_get_full_equip <= 3.0:
        print(f"✅ Numero medio di dungeon per ottenere il full equip per tutto il gruppo: {average_number_of_dungeons_to_get_full_equip:.2f}")
    elif average_number_of_dungeons_to_get_full_equip < 2.7:
        print(f"⚠️ Il numero medio di dungeon per ottenere il full equip è troppo basso! ({average_number_of_dungeons_to_get_full_equip:.2f}). Il valore ottimale è compreso tra 2.7 e 3.0.")
    elif average_number_of_dungeons_to_get_full_equip > 3.0:
        print(f"⚠️ Il numero medio di dungeon per ottenere il full equip è troppo alto! ({average_number_of_dungeons_to_get_full_equip:.2f}). Il valore ottimale è compreso tra 2.7 e 3.0.")

    # Test sul danno medio in un dungeon facile
    if average_damage_to_single_chatacter_in_easy_dungeon >= 21 and average_damage_to_single_chatacter_in_easy_dungeon <= 22:
        print(f"✅ Danno medio in un dungeon facile: {average_damage_to_single_chatacter_in_easy_dungeon:.2f}")
    elif average_damage_to_single_chatacter_in_easy_dungeon < 21:
        print(f"⚠️ Il danno medio in un dungeon facile è troppo basso! ({average_damage_to_single_chatacter_in_easy_dungeon:.2f}). Il valore ottimale è compreso tra 21 e 22.")
    elif average_damage_to_single_chatacter_in_easy_dungeon > 22:
        print(f"⚠️ Il danno medio in un dungeon facile è troppo alto! ({average_damage_to_single_chatacter_in_easy_dungeon:.2f}). Il valore ottimale è compreso tra 21 e 22.")

    # Test sul danno medio in un dungeon medio
    if average_damage_to_single_chatacter_in_medium_dungeon >= 31 and average_damage_to_single_chatacter_in_medium_dungeon <= 32:
        print(f"✅ Danno medio in un dungeon medio: {average_damage_to_single_chatacter_in_medium_dungeon:.2f}")
    elif average_damage_to_single_chatacter_in_medium_dungeon < 31:
        print(f"⚠️ Il danno medio in un dungeon medio è troppo basso! ({average_damage_to_single_chatacter_in_medium_dungeon:.2f}). Il valore ottimale è compreso tra 31 e 33.")
    elif average_damage_to_single_chatacter_in_medium_dungeon > 33:
        print(f"⚠️ Il danno medio in un dungeon medio è troppo alto! ({average_damage_to_single_chatacter_in_medium_dungeon:.2f}). Il valore ottimale è compreso tra 31 e 33.")

    # Test sul numero medio di pozioni di guarigione in un dungeon facile
    if average_number_of_small_healing_potions_in_easy_dungeon >= 3 and average_number_of_small_healing_potions_in_easy_dungeon <= 4:
        print(f"✅ Numero medio di pozioni di guarigione in un dungeon facile: {average_number_of_small_healing_potions_in_easy_dungeon:.2f}")
    elif average_number_of_small_healing_potions_in_easy_dungeon < 3:
        print(f"⚠️ Il numero medio di pozioni di guarigione in un dungeon facile è troppo basso! ({average_number_of_small_healing_potions_in_easy_dungeon:.2f}). Il valore ottimale è compreso tra 3 e 4.")
    elif average_number_of_small_healing_potions_in_easy_dungeon > 4:
        print(f"⚠️ Il numero medio di pozioni di guarigione in un dungeon facile è troppo alto! ({average_number_of_small_healing_potions_in_easy_dungeon:.2f}). Il valore ottimale è compreso tra 3 e 4.")

if __name__ == "__main__":
    main()
