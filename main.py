from hikka import Hikka

api = Hikka("")
print(f'My username: {api.user.search_users("Lor")[0].username}')


