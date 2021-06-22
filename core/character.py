# singletoning for memory optimizations
import json

from core.db.itemDB.items import *


class Character(object):
    """
    representation of a character, only one can exist at any given time in fitting window, storage via json file
    """
    instance = None

    id: int = -1

    talent: list[int] = 5 * [0]  # main, e, q, p1, p2
    constellation: int = 0

    weapon: Weapon

    flower: Feather
    feather: Feather
    watch: Watch
    cup: Cup
    crown: Crown

    def __new__(cls):
        if cls.instance is None:
            print('Creating the object')
            cls.instance = super(Character, cls).__new__(cls)
            # Put any initialization here.
        return cls.instance

    def setChar(self) -> None:
        pass

    def __str__(self) -> str:
        return json.dumps(vars(self))
