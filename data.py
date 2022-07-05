import requests


def getdata():
    r = requests.get("https://api.agify.io?name=meelad")
    if r.ok:
        return r
    else:
        return None