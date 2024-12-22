from units.character import Character

classes = {
    "Fighter": Character(
        name="Fighter", 
        hp=22,
        combat_success_rate=0.11,
        role="Subisci il 20%% danni in meno al prossimo scontro."
    ),
    "Berserker": Character(
        name="Berserker", 
        hp=22,
        combat_success_rate=0.12,
        role="Furia: Sotto il 50%% della salute, la probabilità di successo aumenta del 5%."
    ),
    "Mage": Character(
        name="Mage", 
        hp=20,
        combat_success_rate=0.14,
        role="Rompe sigilli magici e legge tomi antichi. Per spedizione: 1 suggerimento dal master, 1 Scudo magico: Riduce il danno subito da un compagno del 25% per un combattimento."
    ),
    "Healer": Character(
        name="Healer", 
        hp=20,
        combat_success_rate=0.14,
        role="Guarisce gruppo o singolo. Per spedizione: 1 Cura 4 HP a singolo, 2 Cura 2 HP a gruppo."
    ),
    "Explorer": Character(
        name="Explorer", 
        hp=20,
        combat_success_rate=0.1,
        role="Identifica trappole, tesori e porte segrete. 67% probabilità di individuare una trappola e 50% probabilità di disinnescarla."
    ),
}
