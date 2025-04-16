import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f3caa8a69c9d31c951c2639dbe10c85d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "292022",
    "name": "Luna",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "292022"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

'''response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)'''




