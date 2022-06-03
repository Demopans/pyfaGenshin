import requests
from google.cloud import firestore as fireDB

# ToDo: firebase api got updated. Fix it

db1: str = "http://api.genshin.dev/characters"


class FbDB:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(FbDB, cls).__new__(cls)
            # Put any initialization here.
            cls.fdb = fireDB.Client.from_service_account_json("DBKeys/shared.json")

        return cls.instance
