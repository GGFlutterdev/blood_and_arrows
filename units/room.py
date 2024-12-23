from units.chest import Chest

class Room:
    def __init__(self, rare_items=False, uncommon_items=False, common_items=False, has_encounter=False, trick=None, is_reward=False, has_chest=False):
        self.rare_items = rare_items
        self.uncommon_items = uncommon_items
        self.common_items = common_items
        self.has_encounter = has_encounter
        self.trick = trick
        self.items = []
        self.encounter = None
        self.is_reward = is_reward  # Serve per assegnare una probabilità più alta di trovare un oggetto non comune o raro nella stanza
        self.chest = Chest() if has_chest else None

    def __str__(self):
        room_str = (
            f"Room\n"
            f"  - Trick={self.trick}\n"
            f"  - Items={self.items}\n"
            f"  - Encounter={self.encounter}\n"
        )
        
        # Aggiungi il campo Chest solo se la chest esiste
        if self.chest:
            room_str += f"  - Chest={self.chest}\n"
        
        return room_str


    def has_trick(self):
        return self.trick is not None

    def has_encounter(self):
        return self.has_encounter

    def get_trick(self):
        return self.trick if self.has_trick() else "No trick in this room."

    def add_item(self, item):
        self.items.append(item)

    def set_encounter(self, encounter):
        self.encounter = encounter

    def remove_encounter(self):
        self.encounter = None

    def list_items(self):
        return [str(item) for item in self.items]
