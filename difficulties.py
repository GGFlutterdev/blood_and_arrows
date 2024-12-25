import random

difficulties = {
    "Easy": {
        "DSP": lambda: random.randint(1, 6),
        "DSN": lambda: random.randint(1, 8)
    },
    "Medium": {
        "DSP": lambda: random.randint(1, 8) + 1,
        "DSN": lambda: random.randint(1, 10) + 2,
    },
    "Hard": {
        "DSP": lambda: random.randint(1, 10) + random.randint(1, 6),
        "DSN": lambda: random.randint(1, 20)
    },
    "Nightmare": {
        "DSP": lambda: random.randint(1, 12) + random.randint(1, 8),
        "DSN": lambda: random.randint(1, 20) + random.randint(1, 12)
    },
}
