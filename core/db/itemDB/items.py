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
    type: str

    def __init__(self, name: str = "", refine: int = 0, level: int = 0, typ: str = "") -> None:
        self.name = name
        self.refine = refine
        self.level = level  # level modifies mainstat and substat
        self.type = typ

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
            # consider only the first stat as valid
            if mainstat is None:
                mainstat = {"DEF%": 0}
            else:
                mainstat = {list(mainstat.keys())[0]: mainstat[list(mainstat.keys())[0]]}

        self.mainstat = mainstat
        self.name = name
        self.level = level
        self.substats = {} if substats is None else substats


class Flower(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        if "HP" not in mainstat.keys():
            mainstat = {"HP": mainstat[list(mainstat.keys())[0]]}
        super(Flower, self).__init__(name, level, mainstat, substats)


class Feather(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        if "ATK" not in mainstat.keys():
            mainstat = {"ATK": mainstat[list(mainstat.keys())[0]]}
        super(Feather, self).__init__(name, level, mainstat, substats)


class Watch(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        super(Watch, self).__init__(name, level, mainstat, substats)


class Cup(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        super(Cup, self).__init__(name, level, mainstat, substats)


class Crown(GenericArtifact):
    def __init__(self, name: str = "", level: int = 0, mainstat: dict[str, float] = None,
                 substats: dict[str, float] = None):
        super(Crown, self).__init__(name, level, mainstat, substats)
