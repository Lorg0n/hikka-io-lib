[<img src="https://rosset-nocpes.github.io/ua-badges/src/powered-by-hikka.svg">](https://hikka.io/)

# hikka-io-lib
The library allows you to interact with the API from hikka.io in a more understandable way
## Installation

You can install **hikka-io-lib** using git and terminal:

```bash
pip install git+https://github.com/Lorg0n/hikka-io-lib/
```

## Authorisation
How to get auth code to use methods associated with your profile
1. Copy the value of the `Auth` header from F12 menu.
![img.png](img/img.png)
2. Put this in the arguments, during the initialisation of the Hikka class object. Example:
```python
from hikka import Hikka

api = Hikka("YGH*******************IRc")
print(f'My username: {api.me().username}')

# My username: Lorg0n
```

## Usage

Here's how you can use **hikka-io-lib** in your Python code:

```python
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
```

## TODO

- [X] Add authorisation
    - [X] Add methods that require authorisation
- [ ] Implement all remaining methods
- [ ] Add comments for each method

## Documentation

The official documentation can be found at [api.hikka.io](https://api.hikka.io/docs#)

## Contributing

If you'd like to contribute to this library, please fork the repository and create a pull request. You can also open an issue if you find any bugs or have any feature requests.
