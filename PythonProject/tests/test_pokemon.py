import requests
import pytest

URL = "https://api.pokemonbattle.ru"
TOKKEN = "2c66bd75cc07c7d2ed4dc9de8d86a93c"
HEADER = {"Content-Type" : "application/json", "trainer_token" : TOKKEN}
TRAINER_ID = "4499"

def test_status_code():
    response = requests.get(url=f'{URL}/v2/trainers')
    assert response.status_code == 200

def test_trainer_id():
    response = response = requests.get(url=f'{URL}/v2/trainers', params={'trainer_id' : TRAINER_ID})
    
    assert response.json()['data'][0]['id'] == TRAINER_ID

