import json
from functools import singledispatchmethod

import requests

HIKKA_URL_BASE = "https://api.hikka.io"


class Genre:
    def __init__(self, data):
        self.name_ua = data.get("name_ua", "")
        self.name_en = data.get("name_en", "")
        self.slug = data.get("slug", "")
        self.type = data.get("type", "")


class Company:
    def __init__(self, data):
        self.company = data.get("company", {})
        self.type = data.get("type", "")


class Character:
    @singledispatchmethod
    def __init__(self, data):
        # self.main = data.get("main", False)
        self.name_ua = data["character"].get("name_ua", "")
        self.name_en = data["character"].get("name_en", "")
        self.name_ja = data["character"].get("name_ja", "")
        self.image = data["character"].get("image", "")
        self.slug = data["character"].get("slug", "")
        self.synonyms = data["character"].get("synonyms", [])

    @classmethod
    def from_finder_dict(cls, data):
        data = {
            "character": {
                "name_ua": data.get("name_ua", ""),
                "name_en": data.get("name_en", ""),
                "name_ja": data.get("name_ja", ""),
                "image": data.get("image", ""),
                "slug": data.get("slug", ""),
                "synonyms": data.get("name_", []),
            }
        }
        return cls(data)


class Person:
    def __init__(self, data):
        self.name_native = data["person"].get("name_native", "")
        self.name_ua = data["person"].get("name_ua", "")
        self.name_en = data["person"].get("name_en", "")
        self.image = data["person"].get("image", "")
        self.slug = data["person"].get("slug", "")
        self.synonyms = data["person"].get("synonyms", [])
        self.roles = [Role(role_data) for role_data in data.get("roles", [])]

    def __str__(self):
        return f"<Person:{self.name_en} ({self.name_ua})>"


class Role:
    def __init__(self, data):
        self.name_ua = data.get("name_ua", "")
        self.name_en = data.get("name_en", "")
        self.weight = data.get("weight", 0)
        self.slug = data.get("slug", "")


class Episode:
    def __init__(self, data):
        self.aired = data.get("aired", 0)
        self.title_ua = data.get("title_ua", "")
        self.title_en = data.get("title_en", "")
        self.title_ja = data.get("title_ja", "")
        self.index = data.get("index", 0)

    def __str__(self):
        return f"<Episode: {self.title_en} ({self.title_ja}) - Episode {self.index}>"


class Anime:
    def __init__(self, data):
        self.companies = [Company(company_data) for company_data in data.get("companies", [])]
        self.genres = [Genre(genre_data) for genre_data in data.get("genres", [])]
        self.comments_count = data.get("comments_count", 0)
        self.start_date = data.get("start_date", 0)
        self.end_date = data.get("end_date", 0)
        self.episodes_released = data.get("episodes_released", 0)
        self.episodes_total = data.get("episodes_total", 0)
        self.synopsis_en = data.get("synopsis_en", "")
        self.synopsis_ua = data.get("synopsis_ua", "")
        self.media_type = data.get("media_type", "")
        self.title_ua = data.get("title_ua", "")
        self.title_en = data.get("title_en", "")
        self.title_ja = data.get("title_ja", "")
        self.duration = data.get("duration", 0)
        self.poster = data.get("poster", "")
        self.status = data.get("status", "")
        self.source = data.get("source", "")
        self.rating = data.get("rating", "")
        self.has_franchise = data.get("has_franchise", False)
        self.scored_by = data.get("scored_by", 0)
        self.score = data.get("score", 0.0)
        self.nsfw = data.get("nsfw", False)
        self.slug = data.get("slug", "")
        self.season = data.get("season", "")
        self.year = data.get("year", 0)
        self.synonyms = data.get("synonyms", [])
        self.external = data.get("external", [])
        self.videos = data.get("videos", [])
        self.ost = data.get("ost", [])
        self.stats = data.get("stats", {})
        self.schedule = data.get("schedule", [])
        self.translated_ua = data.get("translated_ua", False)
        self.updated = data.get("updated", 0)


class User:
    def __init__(self, data):
        self.reference = data.get("reference", "")
        self.updated = data.get("updated", 0)
        self.description = data.get("description", "")
        self.username = data.get("username", "")
        self.created = data.get("created", 0)
        self.cover = data.get("cover", "")
        self.active = data.get("active", False)
        self.avatar = data.get("avatar", "")
        self.role = data.get("role", "")

    def __str__(self):
        return f"<User: {self.username} ({self.role})>"


class WatchHistoryItem:
    def __init__(self, data):
        self.content = data.get("content", {})
        self.history_type = data.get("history_type", "")
        self.created = data.get("created", 0)
        self.updated = data.get("updated", 0)
        self.reference = data.get("reference", "")
        self.data = data.get("data", {})

    def __str__(self):
        return f"<Watch History Item: {self.reference}>"


class ActionData:
    def __init__(self, timestamp, actions):
        self.timestamp = timestamp
        self.actions = actions

    def __str__(self):
        return f"<ActionData(timestamp={self.timestamp}, actions={self.actions})>"


class Hikka:
    def __init__(self, auth=None):
        self.auth = auth

    @property
    def genres(self):
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/anime/genres")
        result = []
        for i in result_json["list"]:
            genre = Genre(i)
            result.append(genre)
        return result

    def find_users(self, query):
        result_json = _post_json_from_url(f"{HIKKA_URL_BASE}/user/list", json={
            "query": query
        })
        return [User(users_data) for users_data in result_json]

    def get_user_activity(self, username):
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/user/{username}/activity")
        return [ActionData(item["timestamp"], item["actions"]) for item in result_json]

    def get_user_history(self, username, page=1, size=15):
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/user/{username}/history?page={page}&size={size}")
        return [WatchHistoryItem(item) for item in result_json["list"]]

    def get_user(self, username):
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/user/{username}")
        return User(result_json)

    def me(self):
        if self.auth is None:
            return None

        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/user/me", headers={
            "auth": self.auth
        })
        return User(result_json)

    def get_voices_by_character(self, slug, page=1, size=15):
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/characters/{slug}/voices?page={page}&size={size}")
        return [Person(person_data) for person_data in result_json["list"]]

    def get_anime_by_character(self, slug, page=1, size=15):
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/characters/{slug}/anime?page={page}&size={size}")
        return [Anime(anime_data["anime"]) for anime_data in result_json["list"]]

    def find_characters(self, query, page=1, size=15):
        result_json = _post_json_from_url(f"{HIKKA_URL_BASE}/characters?page={page}&size={size}", json={
            "query": query
        })
        return [Character.from_finder_dict(character_data) for character_data in result_json["list"]]

    def get_episodes(self, slug, page=1, size=15):
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/anime/{slug}/episodes?page={page}&size={size}")
        return [Episode(episode_data) for episode_data in result_json["list"]]

    def get_stuff(self, slug, page=1, size=15):
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/anime/{slug}/staff?page={page}&size={size}")
        return [Person(person_data) for person_data in result_json["list"]]

    def get_characters(self, slug, page=1, size=15):
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/anime/{slug}/characters?page={page}&size={size}")
        return [Character(character_data) for character_data in result_json["list"]]

    def get_anime_info(self, slug):
        result_json = _get_json_from_url(f"{HIKKA_URL_BASE}/anime/{slug}")
        # print(json.dumps(result_json, indent=4, ensure_ascii=False))
        return Anime(result_json)


def _post_json_from_url(url, json):
    try:
        r = requests.post(url, json=json)
        r.raise_for_status()
        result_json = r.json()
    except requests.RequestException as e:
        raise f"Error executing the request: {e}"

    return result_json


def _get_json_from_url(url, headers=None):
    try:
        if headers is None:
            r = requests.get(url)
        else:
            r = requests.get(url, headers=headers)
        r.raise_for_status()
        result_json = r.json()
    except requests.RequestException as e:
        raise f"Error executing the request: {e}"

    return result_json
