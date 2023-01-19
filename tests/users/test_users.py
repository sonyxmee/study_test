import requests
import pytest

from configurations import URL
from src.baseclass.response import Response
from src.generators.player_localize import PlayerLocalize
from src.pydantic_schemas.user import User
from src.enum.user_enums import StatusEnum


@pytest.mark.development
@pytest.mark.skip
def test_request_post(get_users):
    response = Response(get_users)
    response.assert_status_code(200).validate(User)


@pytest.mark.development
@pytest.mark.parametrize('status', [
    *StatusEnum.get_status_list()
])
def test_set_status_player(get_player, status):
    print(get_player.set_status(status).build())


@pytest.mark.development
@pytest.mark.parametrize('value', [
    'account_status',
    'balance',
    'avatar',
    'localize'
])
def test_del_player(get_player, value):
    del get_player.build()[value]
    print(get_player.build())


def test_generator_localize(get_player):
    print(get_player.update_localize(PlayerLocalize('en_US').set_age(20)).build())


@pytest.mark.parametrize('keys, lang', [('fr', 'fr_FR')])
def test_upd_inner_value(get_player, keys, lang):
    print(f'keys = {keys}')
    print(get_player.update_inner_value(
        ['localize', keys, 'gut'],
        PlayerLocalize(lang).set_age(20).build()
    ).build())
