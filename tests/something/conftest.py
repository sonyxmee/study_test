import pytest
from random import randrange


def _calculate(a, b):
    return a + b


# тк в фикстуру нельзя передать параметры, то можно создать еще одну функцию и с пом. нее выполнить необходимое
@pytest.fixture
def calculate():
    return _calculate


"""
пример Setup and Teardown
используется при коннекте с БД или при создании юзера
"""

@pytest.fixture
def generate_number():
    print('Number is generating')
    number = randrange(1, 50, 2)
    print('Number generated')
    yield  # передача управления тесту
    # тест отрабатывет, и после возвращается в фикстуру и заканчивает ее
    print('Fixture done')
