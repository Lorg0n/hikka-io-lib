import hikka as hk
from hikka.utils import *

class Follow:
    def __init__(self, hikka):
        if not isinstance(hikka, hk.Hikka):
            raise TypeError("Hikka must be an instance of class Hikka")
        self.hikka = hikka

    def check_follow(self, username):
        if not self.hikka.is_authenticated:
            raise ValueError("Hikka must be authenticated")

        try:
            respond = request(f"{HIKKA_URL_BASE}/follow/{username}", "GET")
            return respond["follow"]
        except:
            return False

    # def follow_user(self, username):
    #     if not self.hikka.is_authenticated:
    #         raise ValueError("Hikka must be authenticated")
    #
    # def unfollow_user(self, username):
    #     if not self.hikka.is_authenticated:
    #         raise ValueError("Hikka must be authenticated")
    #
    # def get_follow_stats(self, username):
    #     if not self.hikka.is_authenticated:
    #         raise ValueError("Hikka must be authenticated")
    #
    # def get_followed_users(self, username):
    #     if not self.hikka.is_authenticated:
    #         raise ValueError("Hikka must be authenticated")
    #
    # def get_followers(self, username):
    #     if not self.hikka.is_authenticated:
    #         raise ValueError("Hikka must be authenticated")