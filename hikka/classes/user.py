from hikka.utils import *
import hikka as hk


class UserResponse:
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


class User:
    def __init__(self, hikka):
        if not isinstance(hikka, hk.Hikka):
            raise TypeError("Hikka must be an instance of class Hikka")
        self.hikka = hikka
        self._user_history_pagination = {}

    def get_me(self):
        if not self.hikka.is_authenticated:
            raise ValueError("Hikka must be authenticated")

        result_json = request(f"{HIKKA_URL_BASE}/user/me", "GET", headers={
            "auth": self.hikka.auth
        })
        return UserResponse(result_json)

    def get_user_profile(self, username):
        result_json = request(f"{HIKKA_URL_BASE}/user/{username}", "GET")
        return UserResponse(result_json)

    def get_user_history(self, username, page=1, size=15):
        result_json = request(f"{HIKKA_URL_BASE}/user/{username}/history?page={page}&size={size}", "GET")
        self._user_history_pagination[username] = result_json["pagination"]
        return [WatchHistoryItem(item) for item in result_json["list"]]

    def user_history_pagination(self, username):
        if self._user_history_pagination[username] is None:
            self.get_user_history(self, username)
        return self._user_history_pagination[username]

    def get_user_activity(self, username):
        result_json = request(f"{HIKKA_URL_BASE}/user/{username}/activity", "GET")
        return [ActionData(item["timestamp"], item["actions"]) for item in result_json]

    def search_users(self, query):
        result_json = request(f"{HIKKA_URL_BASE}/user/list", "POST", json={
            "query": query
        })
        return [UserResponse(users_data) for users_data in result_json]

