import requests

root: str = "http://api.genshin.dev/characters"


def updateChars():
    r: requests.Response = requests.get(root)
    try:
        r.raise_for_status()
        # Code here will only run if the request is successful, skip updating db if api call fails
        # build character db
        tmp = dict()
        for i in r.json():
            tmp[i] = requests.get(root + i).content

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
