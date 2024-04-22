from hikka import Hikka

api = Hikka()
for character in api.find_characters("naruto"):
    character_slug = character.slug
    for anime in api.get_anime_by_character(character_slug):
        print(f"{character.name_ja}: in anime \"{anime.title_ja}\"")

# うずまき ナルト: in anime "Road of Naruto"
# うずまき ナルト: in anime "Naruto: Shippuuden"
# うずまき ナルト: in anime "Naruto"
# うずまき ナルト: in anime "The Last: Naruto the Movie"
# うずまき ナルト: in anime "Naruto: Shippuuden Movie 6 - Road to Ninja"
# うずまき ナルト: in anime "Naruto: Shippuuden - Sunny Side Battle"
# ...