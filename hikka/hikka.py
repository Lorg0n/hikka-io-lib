import requests

HIKKA_URL_BASE = "https://api.hikka.io"


class Genre:
    def __init__(self, name_ua, name_en, slug, type):
        self.name_ua = name_ua
        self.name_en = name_en
        self.slug = slug
        self.type = type


class GenreList:
    def __init__(self):
        self.__list = []

    def add(self, item: Genre):
        self.__list.append(item)

    @property
    def list(self):
        return self.__list


class Hikka:
    def __init__(self):
        pass

    @property
    def genres(self):
        genre_list = GenreList()
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/anime/genres")

        for i in result_json["list"]:
            genre = Genre(i["name_ua"], i["name_en"], i["slug"], i["type"])
            genre_list.add(genre)

        return genre_list

    def get_anime_info(self, slug):
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/anime/{slug}")
        print(f"{HIKKA_URL_BASE}/anime/{slug}")
        print(result_json)


def _get_json_from_url(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        result_json = r.json()
    except requests.RequestException as e:
        raise f"Error executing the request: {e}"

    return result_json
