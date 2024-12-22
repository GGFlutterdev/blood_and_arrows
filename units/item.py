class Item:
    def __init__(self, name: str, slot: str, item_class: list, rarity: str, effect: str):
        self.name = name
        self.slot = slot
        self.item_class = item_class
        self.rarity = rarity
        self.effect = effect

    def __str__(self):
        return (
            f"\n    - Item(name={self.name}, slot={self.slot}, "
            f"class={self.item_class}, rarity={self.rarity}, effect={self.effect})"
        )

    def __repr__(self):
        return self.__str__()
