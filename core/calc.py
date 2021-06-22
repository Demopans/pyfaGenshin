# ulti file containing all functions needed to calc stats
from core.character import *


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
                   char.cup.substats.get(stat, 0) + \
                   char.weapon.substat.get(stat, 0)
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
        # calc hp
        pass

    @staticmethod
    def calcAtk(char: Character) -> int:
        atk: int = int(sumAll(char, "ATK"))
        atkp: float = sumAll(char, "ATK%")

        pass

    @staticmethod
    def calcDef(char: Character) -> int:
        de: int = int(sumAll(char, "DEF"))
        dep: float = sumAll(char, "DEF%")
        pass

    @staticmethod
    def calcEM(char: Character) -> int:
        EM: int = int(sumAll(char, "EM"))
        pass

    @staticmethod
    def calcCritR(char: Character) -> int:
        cr: int = int(sumAll(char, "Crit Rate"))
        pass

    @staticmethod
    def calcCritD(char: Character) -> int:
        cd: int = int(sumAll(char, "Crit Dmg"))
        pass


def calcHPBoost(char: Character):
    pass


def calcIncHP(char: Character):
    pass


def calcER(char: Character):
    pass


def calcCDRed(char: Character):
    pass


def calcShieldBoost(char: Character):
    pass


def calcDMGBoost(char: Character):
    pass


def calcResistBoost(char: Character):
    pass