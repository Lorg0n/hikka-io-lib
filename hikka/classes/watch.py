import hikka as hk
from hikka.utils import *


class AnimeRecord:
    def __init__(self, data):
        self.reference = data.get('reference')
        self.note = data.get('note')
        self.updated = data.get('updated')
        self.created = data.get('created')
        self.status = data.get('status')
        self.rewatches = data.get('rewatches')
        self.duration = data.get('duration')
        self.episodes = data.get('episodes')
        self.score = data.get('score')
        anime_data = data.get('anime', {})
        self.media_type = anime_data.get('media_type')
        self.title_ua = anime_data.get('title_ua')
        self.title_en = anime_data.get('title_en')
        self.title_ja = anime_data.get('title_ja')
        self.episodes_released = anime_data.get('episodes_released')
        self.episodes_total = anime_data.get('episodes_total')
        self.poster = anime_data.get('poster')
        self.anime_status = anime_data.get('status')
        self.scored_by = anime_data.get('scored_by')
        self.anime_score = anime_data.get('score')
        self.slug = anime_data.get('slug')
        self.translated_ua = anime_data.get('translated_ua')
        self.season = anime_data.get('season')
        self.source = anime_data.get('source')
        self.rating = anime_data.get('rating')
        self.year = anime_data.get('year')


class Watch:
    def __init__(self, hikka):
        if not isinstance(hikka, hk.Hikka):
            raise TypeError("Hikka must be an instance of class Hikka")
        self.hikka = hikka
        self._user_watch_list_pagination = {}

    def check_follow(self, username):
        if not self.hikka.is_authenticated:
            raise ValueError("Hikka must be authenticated")

        try:
            respond = request(f"{HIKKA_URL_BASE}/follow/{username}", "GET")
            return respond["follow"]
        except:
            return False

    def get_watch_by_slug(self, slug):
        if not self.hikka.is_authenticated:
            raise ValueError("Hikka must be authenticated")

        respond = request(f"{HIKKA_URL_BASE}/watch/{slug}", "GET", headers={
            "auth": self.hikka.auth,
            "slug": slug,
        })
        return AnimeRecord(respond)


    # def add_watch_by_slug(self, slug):
    #     pass
    #
    # def delete_watch_by_slug(self, slug):
    #     pass
    #
    # def get_following_by_watch_slug(self, slug):
    #     pass
    #
    # def get_user_watch_list_stats(self, username):
    #     pass
    #
    # def get_random_watch_entry(self, username, status):
    #     pass

    def get_user_watch_list(self, username, page=1, size=15):
        result_json = request(f"{HIKKA_URL_BASE}/watch/{username}/list?page={page}&size={size}", "POST", json={})
        self._user_watch_list_pagination[username] = result_json["pagination"]
        return [AnimeRecord(record_data) for record_data in result_json["list"]]

    def get_user_watch_list_pagination(self, username, size=15):
        if username not in self._user_watch_list_pagination:
            self.get_user_watch_list(username, size=size)
        return self._user_watch_list_pagination[username]
