from core.character.calc import *
from src.core.character.character import Character


def burstBoost(char: Character):
    atk: int = 0  # replace with getter for base value
    atkp: float = 0  # replace with getter for base vals
    return getStats(char.name, char.level).__getitem__(1) * (atkp / 100) + atk
