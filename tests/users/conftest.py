import pytest
import requests
from configurations import URL
from src.generators.player import Player

"""
    scope='function'
        - по умолчанию
        - вызывается каждый раз при запуске теста
        'session'
        - используется при авторизации пользователя и в др. случаях
    autouse
        - по умолчанию False
        - True -> фикстура будет вызывается при запуске любого теста
"""


@pytest.fixture
def get_users():
    resp = requests.get(url=URL)
    return resp


# value of function save in temp -> test_function(temp)

@pytest.fixture
def get_player():
    return Player()
