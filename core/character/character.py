# singletoning for memory optimizations
import json

from core.db.itemDB.items import *


class Character(object):
    """
    representation of a character, only one can exist at any given time in fitting window, storage via json file
    """
    instance = None

    name: str
    level: int
    talent: tuple[int, int, int, int, int]  # main, e, q, p1, p2
    constellation: int

    weapon: Weapon

    flower: Feather
    feather: Feather
    watch: Watch
    cup: Cup
    crown: Crown

    def __init__(self, name: str = "Albedo", level: int = 1, talent: tuple[int, int, int, int, int] = None,
                 constellation: int = 0):
        """
        Default constructor that supports the comparison of multiple fittings.
        """
        if talent is None:
            talent = (1, 1, 1, 0, 0)

        self.name = name
        self.level = level
        self.talent = talent
        self.constellation = constellation

    def setChar(self) -> None:
        pass

    def __str__(self) -> str:
        return json.dumps(vars(self))