from genshinstats import *
import requests

from core.db.characterDB.charDB import updateChars

root: str = "http://api.genshin.dev"


def dbNeedsUpdate():
    # get version header of db, and compare with that of the api
    # db only has the data required for fitting
    pass


def updateDB() -> None:
    def updateWeaps():
        r: requests.Response = requests.get(root + "/weapons")
        try:
            r.raise_for_status()
            # Code here will only run if the request is successful, skip updating db if api call fails
            # build character db
            r.json()

        except requests.exceptions.HTTPError as errh:
            print(errh)
            return
        except requests.exceptions.ConnectionError as errc:
            print(errc)
            return
        except requests.exceptions.Timeout as errt:
            print(errt)
            return
        except requests.exceptions.RequestException as err:
            print(err)
            return

    updateChars()
    updateWeaps()

    pass
