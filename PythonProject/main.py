import requests

URL = "https://api.pokemonbattle.ru"
TOKKEN = "2c66bd75cc07c7d2ed4dc9de8d86a93c"
HEADER = {"Content-Type" : "application/json", "trainer_token" : TOKKEN}

Body_Create = {
    "name": "Бабуленька",
    "photo_id": 46
}

Body_Rename = {
    "pokemon_id": "42550",
    "name": "Бабка",
    "photo_id": 46
}

Body_PokemonInPokebol = {
    "pokemon_id": "42550"
}

Create_Pokemon = requests.post(url=f'{URL}/v2/pokemons', headers=HEADER, json=Body_Create)
print(Create_Pokemon.text)

Rename_Pokemon = requests.put(url=f'{URL}/v2/pokemons', headers=HEADER, json=Body_Rename)
print(Rename_Pokemon.text)

Catch_Pokemon = requests.post(url=f'{URL}/v2/trainers/add_pokeball', headers=HEADER, json=Body_PokemonInPokebol)
print(Catch_Pokemon.text)
