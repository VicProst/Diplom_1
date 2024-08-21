import pytest
from unittest.mock import Mock


@pytest.fixture
def new_bun_mock():
    bun_mock = Mock()
    bun_mock.name = 'Crunchie bun'
    bun_mock.price = 12.5
    bun_mock.get_name.return_value = bun_mock.name
    bun_mock.get_price.return_value = bun_mock.price
    return bun_mock

@pytest.fixture
def new_ingredient_mock(ingredient_type):
    ingredient_one_mock = Mock()
    ingredient_one_mock.ingredient_type = ingredient_type
    ingredient_one_mock.name = 'Spicy-X'
    ingredient_one_mock.price = 1.5
    ingredient_one_mock.get_type.return_value = ingredient_one_mock.ingredient_type
    ingredient_one_mock.get_name.return_value = ingredient_one_mock.name
    ingredient_one_mock.get_price.return_value = ingredient_one_mock.price
    ingredient_two_mock = Mock()
    ingredient_two_mock.ingredient_type = ingredient_type
    ingredient_two_mock.name = 'Сыр с астероидной плесенью'
    ingredient_two_mock.price = 5.5
    ingredient_two_mock.get_type.return_value = ingredient_two_mock.ingredient_type
    ingredient_two_mock.get_name.return_value = ingredient_two_mock.name
    ingredient_two_mock.get_price.return_value = ingredient_two_mock.price
    return ingredient_one_mock, ingredient_two_mock
