import pytest
from random import randrange


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return None


#
@pytest.fixture
def calculate():
    """
    тк в фикстуру нельзя передать параметры,
    то можно создать еще одну функцию и с пом. нее выполнить необходимое
    """
    return _calculate


@pytest.fixture
def generate_number():
    print('Number is generating')
    number = randrange(1, 50, 2)
    print('Number generated')
    yield  # передача управления тесту
    # тест отрабатывет, и после возвращается в фикстуру и заканчивает ее
    print('Fixture done')
    """
    пример Setup and Teardown
    используется при коннекте с БД или при создании юзера
    """


@pytest.fixture
def get_number():
    print('Number is generating')
    number = randrange(1, 50, 2)
    return number


@pytest.fixture
def get_indirect_data(request):
    """
    фикстура, в которую передаются параметры из теста
    """
    if request.param == 'scenario_1':
        return {'name': 'John'}
    elif request.param == 'scenario_2':
        return {'name': 'Katya'}
    else:
        return {'name': 'Vanya'}


@pytest.fixture
def get_sum(get_number):
    """
    на вход подается фикстура
    есть вложенная функция, которая на вход принимает еще одно число для вычислений
    как итог функция get_sum возвращает результат функции _wrapped
    """

    print(f'Getting number: {get_number}')

    def _wrapped(add_number):
        return get_number + add_number

    return _wrapped
