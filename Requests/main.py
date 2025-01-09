import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8e2c643be1805438931695abe6267f66'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "рома",
    "photo_id": 9
}
body_change = {  
    "pokemon_id": "106056",
    "name": "никита",
    "photo_id": 2
}
body_addpokeball = {
    "pokemon_id": "107340"
}

response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.status_code, response_create.text)

response_change = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change)  
print(response_change.status_code, response_change.text)

response_addpokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_addpokeball)
print(response_addpokeball.status_code, response_addpokeball.text)
