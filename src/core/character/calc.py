# ulti file containing all functions needed to calc stats
from src.core.character import character
from src.core.character.character import Character
from core.db.characterDB.charDB import *


# calcs all initial stats on character screen
def sumAll(char: Character, stat: str) -> float:
    sigma: float = char.flower.mainstat.get(stat, 0) + \
                   char.flower.substats.get(stat, 0) + \
                   char.feather.mainstat.get(stat, 0) + \
                   char.feather.substats.get(stat, 0) + \
                   char.watch.mainstat.get(stat, 0) + \
                   char.watch.substats.get(stat, 0) + \
                   char.crown.mainstat.get(stat, 0) + \
                   char.crown.substats.get(stat, 0) + \
                   char.cup.mainstat.get(stat, 0) + \
                   char.cup.substats.get(stat, 0)
    return sigma


class base:
    """
    Holds general stats
    """

    @staticmethod
    def calcHP(char: Character) -> int:
        # formula = (1 + Σ hp%) + Σ hp
        # get all hp stats from equipment
        hp: int = int(sumAll(char, "HP"))
        hpp: float = sumAll(char, "HP%")
        return int((getStats(char.name, char.level).__getitem__(0) * char.weapon.substat.get("HP%")) * hpp + hp)

    @staticmethod
    def calcAtk(char: Character) -> float:
        atk: int = int(sumAll(char, "ATK"))
        atkp: float = sumAll(char, "ATK%")
        return getStats(char.name, char.level).__getitem__(1) * (atkp / 100) + atk

    @staticmethod
    def calcDef(char: Character) -> int:
        de: int = int(sumAll(char, "DEF"))
        dep: float = sumAll(char, "DEF%")
        return int(getStats(char.name, char.level).__getitem__(2) * (dep / 100) + de)

    @staticmethod
    def calcEM(char: Character) -> int:
        return int(sumAll(char, "EM"))
        pass

    @staticmethod
    def calcCritR(char: Character) -> float:
        return sumAll(char, "Crit Rate")
        pass

    @staticmethod
    def calcCritD(char: Character) -> float:
        return sumAll(char, "Crit Dmg")

    @staticmethod
    def calcER(char: Character) -> float:
        return sumAll(char, "ER")

    @staticmethod
    def calcHPBoost(char: Character):
        pass

    @staticmethod
    def calcIncHP(char: Character):
        pass

    @staticmethod
    def calcCDRed(char: Character):
        pass

    @staticmethod
    def calcShieldBoost(char: Character):
        pass

    @staticmethod
    def calcDMGBoost(char: Character):
        pass

    @staticmethod
    def calcResistBoost(char: Character):
        pass
