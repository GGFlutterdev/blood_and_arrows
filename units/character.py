class Character:
    def __init__(name, hp, combat_success_rate, abilities=None):
        self.hp = hp
        self.combat_success_rate = combat_success_rate
        self.abilities = abilities if abilities is not None else []
