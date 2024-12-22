class Encounter:
    def __init__(self, difficulty: str, monsters: list[str]):
        self.difficulty = difficulty
        self.monsters = monsters

    def __str__(self):
        monsters = ", ".join(self.monsters)
        return f"Encounter(difficulty={self.difficulty}, monsters=[{monsters}])"

    def __repr__(self):
        return self.__str__()
