import requests
import firebase_admin as fireAdmin
import firebase as fireDB
from firebase_admin import firestore
from core.character.character import Character, Weapon

# Use the application default credentials
from firebase_admin.auth import Client
from firebase_admin.credentials import Certificate
from google.cloud.firestore_v1 import *

# ToDo: firebase api got updated. Fix it

db1: str = "http://api.genshin.dev/characters"
db2: str = "http://api.genshin.dev/weapons"


class DB:
    instance = None
    cred: fireAdmin.credentials.Certificate
    db: fireAdmin.auth.Client
    dbNoAuth: fireDB.Database
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(DB, cls).__new__(cls)
            # Put any initialization here.
            cls.cred: Certificate
            cls.cred = fireAdmin.credentials.Certificate('../DBKeys/pyfagenshindb-firebase-adminsdk-nnt83-30c34bd520.json')

            fireAdmin.initialize_app(cls.cred, {'projectId': 'pyfagenshindb', })
            cls.db: Client = firestore.client()

        return cls.instance

    def getAllChar(self):
        r: requests.Response = requests.get(db1)
        try:
            r.raise_for_status()
            # Code here will only run if the request is successful, skip updating db if api call fails
            # build character db
            tmp = dict()
            for i in r.json():
                tmp[i] = requests.get(db1 + i).content
            return tmp

        except IOError as err:
            print(err)
            return

    def accessCharacterData(self, char: Character):
        root: DocumentReference = self.db.document(u'Character/{0}'.format(char.name))

    def accessCharData(self, weapon: Weapon):
        root: CollectionReference = self.db.collection(u'Items/Weapons/{0}'.format(weapon.name))


# get char data not covered by firestore
def updateChars():
    r: requests.Response = requests.get(db1)
    try:
        r.raise_for_status()
        # Code here will only run if the request is successful, skip updating db if api call fails
        # build character db
        tmp = dict()
        for i in r.json():
            tmp[i] = requests.get(db1 + i).content
        print(tmp)

    except IOError as err:
        print(err)
        return


def getStats(name: str, lv: int) -> tuple[int, int, int]:  # hp, atk, def
    pass


if __name__ == '__main__':
    dbref = DB.__new__(DB)  # call first
    dbref
