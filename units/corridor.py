class Corridor:
    def __init__(self, ambush: dict = None, trap: dict = None, has_secret_door: bool = False):
        self.ambush = ambush if ambush else {"damage": None, "description": ""}
        self.trap = trap if trap else {"damage": None, "description": ""}
        self.has_secret_door = has_secret_door

    def __str__(self):
        ambush_info = (
            f"ambush_damage={self.ambush['damage']}, ambush_description={self.ambush['description']}"
            if self.ambush.get("damage") else "ambush=None"
        )
        trap_info = (
            f"trap_damage={self.trap['damage']}, trap_description={self.trap['description']}"
            if self.trap.get("damage") else "trap=None"
        )
        secret_door_info = "secret_door=True" if self.has_secret_door else "secret_door=False"
        return f"Corridor({ambush_info}, {trap_info}, {secret_door_info})"

    def is_trapped(self):
        """Return True if the corridor has either a trap or an ambush."""
        return bool(self.trap.get("damage") or self.ambush.get("damage"))

    def to_dict(self):
        """Convert the Corridor instance to a dictionary."""
        result = {"has_secret_door": self.has_secret_door}
        if self.ambush.get("damage"):
            result["ambush"] = self.ambush
        if self.trap.get("damage"):
            result["trap"] = self.trap
        return result

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Corridor instance from a dictionary."""
        return cls(
            ambush=data.get("ambush", {}),
            trap=data.get("trap", {}),
            has_secret_door=data.get("has_secret_door", False)
        )
