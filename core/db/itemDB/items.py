import json
import sys


""" Artifact constants. array index indicates level. weapon constants are too variable """
# ToDo: move to a database or an xml file. this is a few MB at least!


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


class Feather(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        super(Feather, self).__init__(name, level, mainstat, substats)
        if "ATK" not in mainstat.keys():
            sys.stderr.write("Invalid Feather stats")
            exit(-1)


class Watch(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        # verify correct mainstats
        super(Watch, self).__init__(name, level, mainstat, substats)


class Cup(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        # verify correct mainstats
        super(Cup, self).__init__(name, level, mainstat, substats)


class Crown(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        # verify correct mainstats
        super(Crown, self).__init__(name, level, mainstat, substats)
