import pytest
from src.baseclass.response import Response
from example import computer
from src.pydantic_schemas.computer import Computer

@pytest.mark.skip
def test_another(calculate, generate_number):
    print(calculate)
    print(calculate(1, 3))

@pytest.mark.production
@pytest.mark.skip('Reason of skipping')
def test_equal():
    assert 1 == 1

@pytest.mark.skip
@pytest.mark.development
@pytest.mark.parametrize('first, second, result', [
    (2, 3, 5), (-1, 4, 3), (-5, -2, -7), ('b', 3, None), ('a', 'c', None)
])
def test_calculate(first, second, result, calculate):
    assert calculate(first, second) == result, 'Calculations is not equal to expected.'


"""
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
