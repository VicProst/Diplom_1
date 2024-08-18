from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    # По умолчанию булочки нет
    def test_default_value_bun_none(self):
        burger = Burger()
        assert burger.bun == None

    # По умолчанию список ингридиентов пустой
    def test_default_value_ingredients_empty_line(self):
        burger = Burger()
        assert burger.ingredients == []

    # Добавление новой булочки
    def test_set_buns_set_mock_bun_true(self):
        bun_mock = Mock()
        bun_mock.name = 'Crunchie bun'
        bun_mock.price = 12.5
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun.name == 'Crunchie bun' and burger.bun.price == 12.5

    # Добавление нового ингридиента
    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_add_ingredient_add_mock_ingredient_true(self, ingredient_type):
        ingredient_mock = Mock()
        ingredient_mock.ingredient_type = ingredient_type
        ingredient_mock.name = 'Spicy-X'
        ingredient_mock.price = 1.5
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    # Удаление ингредиента
    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_remove_ingredient_add_mock_ingredient_empty_line(self, ingredient_type):
        ingredient_mock = Mock()
        ingredient_mock.ingredient_type = ingredient_type
        ingredient_mock.name = 'Spicy-X'
        ingredient_mock.price = 1.5
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    # Перемещение ингридиента
    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_move_ingredient_add_two_mock_ingredients_ingredients_swapped(self, ingredient_type):
        ingredient_one_mock = Mock()
        ingredient_one_mock.ingredient_type = ingredient_type
        ingredient_one_mock.name = 'Spicy-X'
        ingredient_one_mock.price = 1.5
        ingredient_two_mock = Mock()
        ingredient_two_mock.ingredient_type = ingredient_type
        ingredient_two_mock.name = 'Сыр с астероидной плесенью'
        ingredient_two_mock.price = 5.5
        burger = Burger()
        burger.add_ingredient(ingredient_one_mock)
        burger.add_ingredient(ingredient_two_mock)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient_two_mock

    # Получение цены
    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_price_add_mock_bun_and_mock_ingredient_true(self, ingredient_type):
        bun_mock = Mock()
        bun_mock.name = 'Crunchie bun'
        bun_mock.price = 12.5
        bun_mock.get_price.return_value = bun_mock.price
        ingredient_mock = Mock()
        ingredient_mock.ingredient_type = ingredient_type
        ingredient_mock.name = 'Spicy-X'
        ingredient_mock.price = 1.5
        ingredient_mock.get_price.return_value = ingredient_mock.price
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == 26.5

    # Получение чека
    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_receipt(self, ingredient_type):
        bun_mock = Mock()
        bun_mock.name = 'Crunchie bun'
        bun_mock.price = 12.5
        bun_mock.get_name.return_value = bun_mock.name
        bun_mock.get_price.return_value = bun_mock.price
        ingredient_mock = Mock()
        ingredient_mock.ingredient_type = ingredient_type
        ingredient_mock.name = 'Spicy-X'
        ingredient_mock.price = 1.5
        ingredient_mock.get_type.return_value = ingredient_mock.ingredient_type
        ingredient_mock.get_name.return_value = ingredient_mock.name
        ingredient_mock.get_price.return_value = ingredient_mock.price
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        burger.get_price()
        assert burger.get_receipt() == (f'(==== Crunchie bun ====)\n= {ingredient_type.lower()} Spicy-X'
                                        f' =\n(==== Crunchie bun ====)\n\n''Price: 26.5')
