class Ability:
    def __init__(
        self,
        description="",
        max_selection=0,
        heal=0,
        pc=0,
        damage_reduction_next_fight=0,
        on_itself=False,
        is_passive=False,
        max_number_of_uses=1,
        number_of_uses=0
    ):
        self.description = description
        self.max_selection = max_selection
        self.heal = heal
        self.pc = pc
        self.damage_reduction_next_fight = damage_reduction_next_fight
        self.on_itself = on_itself
        self.is_passive = is_passive
        self.max_number_of_uses = max_number_of_uses if not is_passive else float('inf')
        self.number_of_uses = number_of_uses

    def _use(self):
        if not self.is_passive and self.number_of_uses >= self.max_number_of_uses:
            raise ValueError("Abilità esaurita: hai raggiunto il numero massimo di utilizzi.")
        self.number_of_uses += 1
    
    def reset_uses(self):
        self.number_of_uses = 0

    def apply_heal(self, targets, value=None):
        self._use()
        value = value or self.heal
        for target in targets:
            target.hp += value
    
    def apply_pc(self, targets, value=None):
        self._use()
        value = value or self.pc
        for target in targets:
            target.combat_score += value
    
    def apply_damage_reduction(self, targets, value=None):
        self._use()
        value = value or self.damage_reduction_next_fight
        for target in targets:
            target.damage_reduction_next_fight = value

    def __str__(self):
        return (
            f"Ability(description={self.description}, max_selection={self.max_selection}, damage={self.damage}, "
            f"heal={self.heal}, pc={self.pc}, damage_reduction_next_fight={self.damage_reduction_next_fight}, "
            f"on_itself={self.on_itself}, is_passive={self.is_passive}, "
            f"max_number_of_uses={self.max_number_of_uses}, number_of_uses={self.number_of_uses})"
        )
