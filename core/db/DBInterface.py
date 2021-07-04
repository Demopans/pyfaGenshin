import firebase_admin
from firebase_admin import credentials, firestore

# Use the application default credentials
from firebase_admin.auth import Client
from firebase_admin.credentials import Certificate
from google.cloud.firestore_v1 import CollectionReference, DocumentReference, DocumentSnapshot


class DB:
    instance = None
    cred: Certificate
    db: Client

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(DB, cls).__new__(cls)
            # Put any initialization here.
            cls.cred = credentials.Certificate('DBKeys/pyfagenshindb-firebase-adminsdk-nnt83-30c34bd520.json')
            firebase_admin.initialize_app(cls.cred, {'projectId': 'pyfagenshindb', })
            cls.db: Client = firestore.client()

        return cls.instance

    def accessArtifacts(self):
        root: DocumentReference = self.db.document(u'Items/Artifacts')
        rt: list[str] = ['Crown', 'Cup', 'Feather', 'Flower', 'Watch']
        for i in rt:
            rootc: DocumentSnapshot = root.collection(i).get()
            for j in rootc:
                j
                pass

    def accessWeapons(self):
        root: DocumentReference = self.db.document(u'Items/Weapons')

    def accessChars(self):
        root: CollectionReference = self.db.collection(u'Characters')

        import requests, json
        rt: str = 'https://api.genshin.dev/characters'
        j: DocumentReference = root.document('Amber')
        j.set({# weapon type is in different db
            'Normal Attack': {
                '1': [36.1,36.1,46.4,47.3,59.3], '2': [39.1,39.1,50.2,51.2,64.2], '3': [42,42,54,55,69],
                '4': [46.2,46.2,59.4,60.5,75.9], '5': [49.1,49.1,63.2,64.4,80.7], '6': [52.5,52.5,67.5,68.8,86.3],
                '7': [57.1,57.1,73.4,74.8,93.8], '8': [61.7,61.7,79.4,80.9,101], '9': [66.4,66.4,85.3,86.9,109],
                '10': [71.4,71.4,91.8,93.5,117], '11': [76.4,76.4,98.3,100,126]
            },
            'Charged Attack': {
                '1': [43.9], '2': [47.4], '3': [51], '4': [56.1], '5': [59.7],
                '6': [63.8], '7': [69.4], '8': [75], '9': [80.6], '10': [86.7],
                '11': [92.8]
            },
            'Charged1 Attack': {
                '1': [124], '2': [133], '3': [143], '4': [155], '5': [164],
                '6': [174], '7': [186], '8': [198], '9': [211], '10': [223],
                '11': [236]
            },
            'Skill': {
            },
            'Burst':{
            }

        }, merge=True)


if __name__ == '__main__':
    '''
    Debug code. disable in final product
    '''
    s: DB = DB()
    s.accessChars()
