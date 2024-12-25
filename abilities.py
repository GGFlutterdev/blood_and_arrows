from units.ability import Ability

abilities = {
    "Motivazione": Ability(
        description="Aumenta di 2 i PC di ogni membro del gruppo gruppo per il prossimo combattimento",
        pc=2,
        max_selection=4,
        max_number_of_uses=1
    ),
    "Furia": Ability(
        description="Appena raggiunto il 50% della vita aumenta aumenta di 5 i PC.",
        pc=5,
        on_itself=True,
        is_passive=True
    ),
    "Scudo magico": Ability(
        description="Un alleato selezionato subirà 2 danni in meno nel prossimo scontro.",
        damage_reduction_next_fight=2,
        max_selection=1,
        max_number_of_uses=1
    ),
    "Benedizione": Ability(
        description="Cura 4 danni ad un alleato.",
        heal=2,
        max_selection=1,
        max_number_of_uses=1
    ),
    "Preghiera guaritrice": Ability(
        description="Cura 2 danni a tutto il gruppo.",
        heal=1,
        max_selection=4,
        max_number_of_uses=2
    )
}