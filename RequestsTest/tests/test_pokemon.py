import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f3caa8a69c9d31c951c2639dbe10c85d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '28693'
TRAINER_NAME = 'Luna'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'level' : '5'})
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    response_json = response.json()

    print("Response JSON:", response_json)

    trainer_name = response_json['data'][0]['trainer_name']
    assert trainer_name == 'Luna'

@pytest.mark.parametrize('key,value',[('name','Luna'),('trainer_id', TRAINER_ID)]) 
def test_parametrize(key, value):
    response_parametrize = requests.get(url= f'{URL}/pokemons',params = {'trainer_id':TRAINER_ID}) 
    assert response_parametrize.json()["data"][0][key] == value    