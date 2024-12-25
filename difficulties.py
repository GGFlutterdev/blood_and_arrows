import random

# Danni per ciascuna difficoltà
# Verificati e bilanciati per garantire una progressione logica

difficulties = {
    "Easy": {
        "DSP": lambda: random.randint(1, 6) - 1,
        "DSN": lambda: random.randint(1, 6) + 2
    },
    "Medium": {
        "DSP": lambda: random.randint(1, 8) + 2,
        "DSN": lambda: random.randint(1, 10) + 2,
    },
    "Hard": {
        "DSP": lambda: random.randint(1, 8) + random.randint(1, 6),
        "DSN": lambda: random.randint(1, 12) + 4
    },
    "Nightmare": {
        "DSP": lambda: random.randint(1, 10) + random.randint(1, 8),
        "DSN": lambda: random.randint(1, 20) + random.randint(1, 10)
    },
}