import requests
import pytest



URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

# Проверка, что ответ приходит с кодом 200
def test_get_trainers_by_level():
    """
    KTI-1. Get trainers by level
    """
    response = requests.get(url=f'{URL}/trainers', params= {'level': 1}, timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

# Набор сценариев c переменными
CASES = [
    (4939, 'Tokyo', 'Saski'),
    (4929, 'Seul', 'Tanya'),
]
@pytest.mark.parametrize('id, city, trainer_name', CASES)
# Проверка, что в ответе приходит твой тренер и его параметры
def test_get_trainers_by_id():
    """
    KTI-1. Get trainers by id
    """
    response = requests.get(url=f'{URL}/trainers', params= {'trainer_id': id}, timeout=5)
    assert response.json()['city'] == city, ''
    assert response.json()['trainer_name'] == trainer_name, ''

