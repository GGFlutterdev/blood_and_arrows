from abilities import abilities
from units.character import Character

classes = {
    "Fighter": Character(
        hp=22,
        combat_success_rate=11,
        abilities=[
            abilities["Motivazione"]
        ]
    ),
    "Berserker": Character(
        hp=22,
        combat_success_rate=12,
        abilities=[
            abilities["Furia"]
        ]
    ),
    "Mage": Character(
        hp=20,
        combat_success_rate=14,
        abilities=[
            abilities["Scudo magico"]
        ]
    ),
    "Healer": Character(
        hp=20,
        combat_success_rate=14,
        abilities=[
            abilities["Benedizione"],
            abilities["Preghiera guaritrice"]
        ]
    ),
    "Explorer": Character(
        hp=20,
        combat_success_rate=10,
        abilities=[]
    ),
}
