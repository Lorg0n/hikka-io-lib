![Powered by Hikka](https://rosset-nocpes.github.io/ua-badges/src/powered-by-hikka.svg)

# hikka-io-lib
The library allows you to interact with the API from hikka.io in a more understandable way
## Installation

You can install **hikka-io-lib** using git and terminal:

```bash
pip install git+https://github.com/Lorg0n/hikka-io-lib/
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

- [ ] Add some sort of authorisation
    - [ ] Add methods that require authorisation
- [ ] Implement all remaining methods
- [ ] Complete the comments for each method

## Documentation

The official documentation can be found at [api.hikka.io](https://api.hikka.io/docs#)

## Contributing

If you'd like to contribute to this library, please fork the repository and create a pull request. You can also open an issue if you find any bugs or have any feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.