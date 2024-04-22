import requests


HIKKA_URL_BASE = "https://api.hikka.io"


class Hikka:
    def __init__(self):
        pass

    @property
    def genres(self):
        r = requests.get(f"{HIKKA_URL_BASE}/anime/genres")
        print(r.text)