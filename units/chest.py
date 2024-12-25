import random

class Chest:
    def __init__(self):
        self.type = self._randomize_chest()

    def _randomize_chest(self):
        probability = random.random()
        if probability < 0.25:
            return "Trap"
        else:
            return "Normal"

    def __str__(self):
        if self.type == "Trap":
            return "C'è un forziere. è una trappola! Infligge 4 danni al giocatore in avanguardia."
        elif self.type == "Normal":
            return "Il forziere si apre in sicurezza. Nessun pericolo qui."