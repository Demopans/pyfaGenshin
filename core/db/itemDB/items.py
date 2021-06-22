import json
import sys

""" Artifact constants. array index indicates level. weapon constants are too variable """
# ToDo: move to a database or an xml file. this is a few MB at least!

artifactCaps: dict[int, dict[str, list[float]]] = {
    1: {
        "HP": [129, 178, 227, 275, 324],
        "ATK": [8, 12, 15, 18, 21],
        "HP%": [3.1, 4.3, 5.5, 6.7, 7.9],
        "ATK%": [3.1, 4.3, 5.5, 6.7, 7.9],
        "DEF%": [3.9, 5.4, 6.9, 8.4, 9.9],
        "Physical DMG%": [3.9, 5.4, 6.9, 8.4, 9.9],
        "Elemental DMG%": [3.1, 4.3, 5.5, 6.7, 7.9],
        "Elemental Mastery": [13, 17, 22, 27, 32],
        "Energy Recharge%": [3.5, 4.8, 6.1, 7.5, 8.8],
        "Crit Rate%": [2.1, 2.9, 3.7, 4.5, 5.3],
        "Crit DMG%": [4.2, 5.8, 7.4, 9.0, 10.5],
        "Healing Bonus%": [2.4, 3.3, 4.3, 5.2, 6.1]
    },
    2: {
        "HP": [258, 331, 404, 478, 551],
        "ATK": [17, 22, 26, 31, 36],
        "HP%": [4.2, 5.4, 6.6, 7.8, 9],
        "ATK%": [4.2, 5.4, 6.6, 7.8, 9],
        "DEF%": [5.2, 6.7, 8.2, 9.7, 11.2],
        "Physical DMG%": [5.2, 6.7, 8.2, 9.7, 11.2],
        "Elemental DMG%": [4.2, 5.4, 6.6, 7.8, 9],
        "Elemental Mastery": [17, 22, 26, 31, 36],
        "Energy Recharge%": [4.7, 6, 7.3, 8.6, 9.9],
        "Crit Rate%": [2.8, 3.6, 4.4, 5.2, 6],
        "Crit DMG%": [5.6, 7.2, 8.8, 10.4, 11.9],
        "Healing Bonus%": [3.2, 4.1, 5.1, 6, 6.9]
    },
    3: {
        "HP": [430, 552, 674, 796, 918, 1040, 1162, 1283, 1405, 1527, 1649, 1771, 1893],
        "ATK": [28, 36, 44, 52, 60, 68, 76, 84, 91, 99, 107, 115, 123],
        "HP%": [5.2, 6.7, 8.2, 9.7, 11.2, 12.7, 14.2, 15.6, 17.1, 18.6, 20.1, 21.6, 23.1],
        "ATK%": [5.2, 6.7, 8.2, 9.7, 11.2, 12.7, 14.2, 15.6, 17.1, 18.6, 20.1, 21.6, 23.1],
        "DEF%": [6.6, 8.4, 10.3, 12.1, 14.0, 15.8, 17.7, 19.6, 21.4, 23.3, 25.1, 27.0, 28.8],
        "Physical DMG%": [6.6, 8.4, 10.3, 12.1, 14.0, 15.8, 17.7, 19.6, 21.4, 23.3, 25.1, 27.0, 28.8],
        "Elemental DMG%": [5.2, 6.7, 8.2, 9.7, 11.2, 12.7, 14.2, 15.6, 17.1, 18.6, 20.1, 21.6, 23.1],
        "Elemental Mastery": [21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 80, 86, 92],
        "Energy Recharge%": [5.8, 7.5, 9.1, 10.8, 12.4, 14.1, 15.7, 17.4, 19.0, 20.7, 22.3, 24.0, 25.6],
        "Crit Rate%": [3.5, 4.5, 5.5, 6.5, 7.5, 8.4, 9.4, 10.4, 11.4, 12.4, 13.4, 14.4, 15.4],
        "Crit DMG%": [7.0, 9.0, 11.0, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8],
        "Healing Bonus%": [4.0, 5.2, 6.3, 7.5, 8.6, 9.8, 10.9, 12.0, 13.2, 14.3, 15.5, 16.6, 17.8]
    },
    4: {
        "HP": [645, 828, 1011, 1194, 1377, 1559, 1742, 1925, 2108, 2291, 2474, 2657, 2839, 3022, 3205, 3388, 3571],
        "ATK": [42, 54, 66, 78, 90, 102, 113, 125, 137, 149, 161, 173, 185, 197, 209, 221, 232],
        "HP%": [6.3, 8.1, 9.9, 11.6, 13.4, 15.2, 17.0, 18.8, 20.6, 22.3, 24.1, 25.9, 27.7, 29.5, 31.3, 33.0, 34.8],
        "ATK%": [6.3, 8.1, 9.9, 11.6, 13.4, 15.2, 17.0, 18.8, 20.6, 22.3, 24.1, 25.9, 27.7, 29.5, 31.3, 33.0, 34.8],
        "DEF%": [7.9, 10.1, 12.3, 14.6, 16.8, 19.0, 21.2, 23.5, 25.7, 27.9, 30.2, 32.4, 34.6, 36.8, 39.1, 41.3, 43.5],
        "Physical DMG%": [7.9, 10.1, 12.3, 14.6, 16.8, 19.0, 21.2, 23.5, 25.7, 27.9, 30.2, 32.4, 34.6, 36.8, 39.1, 41.3,
                          43.5],
        "Elemental DMG%": [6.3, 8.1, 9.9, 11.6, 13.4, 15.2, 17.0, 18.8, 20.6, 22.3, 24.1, 25.9, 27.7, 29.5, 31.3, 33.0,
                           34.8],
        "Elemental Mastery": [25, 32, 39, 47, 54, 61, 68, 75, 82, 89, 97, 104, 111, 118, 125, 132, 139],
        "Energy Recharge%": [7.0, 9.0, 11.0, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7,
                             36.7,
                             38.7],
        "Crit Rate%": [4.2, 5.4, 6.6, 7.8, 9.0, 10.1, 11.3, 12.5, 13.7, 14.9, 16.1, 17.3, 18.5, 19.7, 20.8, 22.0, 23.2],
        "Crit DMG%": [8.4, 10.8, 13.1, 15.5, 17.9, 20.3, 22.7, 25.0, 27.4, 29.8, 32.2, 34.5, 36.9, 39.3, 41.7, 44.1,
                      46.4],
        "Healing Bonus%": [4.8, 6.2, 7.6, 9.0, 10.3, 11.7, 13.1, 14.4, 15.8, 17.2, 18.6, 19.9, 21.3, 22.7, 24.0, 25.4,
                           26.8]
    },
    5: {
        "HP": [717, 920, 1123, 1326, 1530, 1733, 1936, 2139, 2342, 2545, 2749, 2952, 3155, 3358, 3561, 3764, 3967, 4171,
               4374, 4577, 4780],
        "ATK": [47, 60, 73, 86, 100, 113, 126, 139, 152, 166, 179, 192, 205, 219, 232, 245, 258, 272, 285, 298, 311],
        "HP%": [7.0, 9.0, 11.0, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7, 36.7, 38.7,
                40.7, 42.7, 44.6, 46.6],
        "ATK%": [7.0, 9.0, 11.0, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7, 36.7, 38.7,
                 40.7, 42.7, 44.6, 46.6],
        "DEF%": [8.7, 11.2, 13.7, 16.2, 18.6, 21.1, 23.6, 26.1, 28.6, 31, 33.5, 36, 38.5, 40.9, 43.4, 45.9, 48.4, 50.8,
                 53.3, 55.8, 58.3],
        "Physical DMG%": [8.7, 11.2, 13.7, 16.2, 16.2, 21.1, 23.6, 26.1, 28.6, 31, 33.5, 36, 38.5, 40.9, 43.4, 45.9,
                          48.4, 50.8, 53.3, 55.8, 58.3],
        "Elemental DMG%": [7.0, 9.0, 11.0, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7, 36.7,
                           38.7, 40.7, 42.7, 44.6, 46.6],
        "Elemental Mastery": [28, 36, 44, 52, 60, 68, 76, 84, 91, 99, 107, 115, 123, 131, 139, 147, 155, 163, 171, 179,
                              187],
        "Energy Recharge%": [7.8, 10.0, 12.2, 14.4, 16.6, 18.8, 21.0, 23.2, 25.4, 27.6, 29.8, 32.0, 34.2, 36.4, 38.6,
                             40.8, 43.0, 45.2, 47.4, 49.6, 51.8],
        "Crit Rate%": [4.7, 6.0, 7.4, 8.7, 10.0, 11.4, 12.7, 14.0, 15.4, 16.7, 18.0, 19.3, 20.7, 22.0, 23.3, 24.7, 26.0,
                       27.3, 28.7, 30.0, 31.1],
        "Crit DMG%": [9.3, 11.9, 14.6, 17.2, 19.9, 22.5, 25.2, 27.8, 30.5, 33.1, 35.8, 38.4, 41.1, 43.7, 46.3, 49.0,
                      51.6, 54.3, 56.9, 59.6, 62.2],
        "Healing Bonus%": [5.4, 6.9, 8.4, 10.0, 11.5, 13.0, 14.5, 16.1, 17.6, 19.1, 20.6, 22.2, 23.7, 25.2, 26.7, 28.3,
                           29.8, 31.3, 32.8, 34.4, 35.9]
    }
}


class Weapon:
    name: str
    refine: int
    level: int
    mainstat: float
    substat: dict[str, float]

    def __init__(self, name: str = "", refine: int = 0, level: int = 0) -> None:
        self.name = name
        self.refine = refine
        self.level = level  # level modifies mainstat and substat

    def tweakStatbasedOnLv(self, newLvl: int) -> None:
        pass

    def __str__(self) -> str:
        return json.dumps(vars(self))


class GenericArtifact:
    name: str
    level: int
    mainstat: dict[str, float]
    substats: dict[str, float]

    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        if mainstat is None or len(mainstat.keys()) != 1:
            sys.stderr.write("Invalid artifact stats")
            exit(-1)  # ToDo: replace with error handler and exit gracefully to gui once that gets implemented

        self.mainstat = mainstat
        self.name = name
        self.level = level
        self.substats = {} if substats is None else substats

    def verifyArtifact(self) -> bool:
        pass


class Flower(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        super(Flower, self).__init__(name, level, mainstat, substats)
        if "HP" not in mainstat.keys():
            sys.stderr.write("Invalid Flower stats")
            exit(-1)

    def __str__(self) -> str:
        return json.dumps(vars(self))


class Feather(GenericArtifact):

    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        super(Feather, self).__init__(name, level, mainstat, substats)
        if "ATK" not in mainstat.keys():
            sys.stderr.write("Invalid Feather stats")
            exit(-1)

    def __str__(self) -> str:
        return json.dumps(vars(self))


class Watch(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        # verify correct mainstats
        super(Watch, self).__init__(name, level, mainstat, substats)

    def __str__(self) -> str:
        return json.dumps(vars(self))


class Cup(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        # verify correct mainstats
        super(Cup, self).__init__(name, level, mainstat, substats)

    def __str__(self) -> str:
        return json.dumps(vars(self))


class Crown(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        # verify correct mainstats
        super(Crown, self).__init__(name, level, mainstat, substats)

    def __str__(self) -> str:
        return json.dumps(vars(self))