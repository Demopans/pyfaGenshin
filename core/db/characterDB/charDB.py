import requests

root: str = "http://api.genshin.dev/characters"


# get char data not covered by firestore
def updateChars():
    r: requests.Response = requests.get(root)
    try:
        r.raise_for_status()
        # Code here will only run if the request is successful, skip updating db if api call fails
        # build character db
        tmp = dict()
        for i in r.json():
            tmp[i] = requests.get(root + i).content
        print(tmp)

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


def getStats(name: str, lv: int) -> tuple[int, int, int]: #
    pass
