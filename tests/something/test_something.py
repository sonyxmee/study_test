import pytest
from src.baseclass.response import Response
from example import computer
from src.pydantic_schemas.computer import Computer
from src.baseclass.message import get_list_mes


def test_another(calculate, generate_number):
    print(calculate)
    print(calculate(1, 3))
    """
    пример использования фикстуры из файла conftest
    """


@pytest.mark.production
@pytest.mark.skip('Reason of skipping')
def test_equal():
    assert 1 == 1
    """
    пример того, как можно пропускать тест при запуске и маркировать тест
    """


@pytest.mark.development
@pytest.mark.parametrize('first, second, result', [
    (2, 3, 5), (-1, 4, 3), (-5, -2, -7), ('b', 3, None), ('a', 'c', None)
])
def test_calculate(first, second, result, calculate):
    assert calculate(first, second) == result, 'Calculations is not equal to expected.'
    """
    пример того, как можно использовать параметры теста
    """


"""
to run one test function:
    pytest -s -v tests/something::name_def
to run tests for development:
    pytest -s -v -k development tests/something
to run tests for no development:
    pytest -s -v -k "not development" tests/something
    
Параметры запусков теста:
 -v: вывод более детального списка тестов
 -s: вывод всех принтов в логах
 --duration=3: все тесты, выполнение которых занимает больше 3 сек, будут отмечены как slowly
 -vv: подробный вывод с временем 
"""


def test_computer():
    parsed_obj = Computer.parse_obj(computer)
    print(parsed_obj)
    """
    парсится вложенный json объект с помощью pydantic schema
    спарсенный объект имеет множестов различных свойств, доступ к которым можно получить через точку
    """


@pytest.mark.parametrize("value", [1, '2', '234567fghj', [1, 2, 7]], ids=str)
def test_different_params_1(value):
    print(value)
    """
    благодаря параметру ids в консоли корректно выводятся параметры теста
    """


@pytest.mark.parametrize("value", get_list_mes(), ids=str)
def test_different_params_2(value):
    print(value)
    """
    тест, который показывает как работать со списком объектов собственного класса
    см. класс Message
    """


@pytest.mark.parametrize('get_indirect_data', ['scenario_1', 'scenario_2'], indirect=True)
def test_data_indirect(get_indirect_data):
    print(get_indirect_data)
    """
    перебрасывание параметров теста в фикстуру для более сложных действий,
    работает как панель управления
    """

def test_get_sum(get_sum):
    print(get_sum(1))
    """
    пример того как использовать фикстуру, 
    принимающую на вход другую фикстуру и имеющую вложенную функцию 
    параметр функции get_sum попадает во влоденную функцию _wrapped
    """