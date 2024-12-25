import random

difficulties = {
    "Easy": {
        "DSP": lambda: random.randint(1, 6) - 1,
        "DSN": lambda: random.randint(1, 6) + 1
    },
    "Medium": {
        "DSP": lambda: random.randint(1, 8),
        "DSN": lambda: random.randint(1, 8) + 2,
    },
    "Hard": {
        "DSP": lambda: random.randint(1, 8) + random.randint(1, 6),
        "DSN": lambda: random.randint(1, 8) + random.randint(1, 6) + 3,
    },
    "Nightmare": {
        "DSP": lambda: random.randint(1, 10) + random.randint(1, 8) - 3,
        "DSN": lambda: random.randint(1, 20) + random.randint(1, 10) + 5
    },
}
