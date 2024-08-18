import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    # По умолчанию тип ингридиента - 'SAUCE' или 'FILLING'
    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_type_of_ingredient_valid_type_true(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'Spicy-X', 1.5)
        assert ingredient.type == ingredient_type and type(ingredient.type) == str

    # По умолчанию название ингридиента - 'Spicy-X'
    def test_name_of_ingredient_valid_name_true(self):
        ingredient = Ingredient('SAUCE', 'Spicy-X', 1.5)
        assert ingredient.name == 'Spicy-X' and type(ingredient.name) == str

    # По умолчанию цена ингридиента - 1.5
    def test_price_of_ingredient_valid_price_true(self):
        ingredient = Ingredient('SAUCE', 'Spicy-X', 1.5)
        assert ingredient.price == 1.5 and type(ingredient.price) == float

    # Выводит текущую цену ингридиента
    def test_get_price_ingredient_valid_price_true(self):
        ingredient = Ingredient('FILLING', 'Сыр с астероидной плесенью', 5.5)
        assert ingredient.get_price() == 5.5 and type(ingredient.get_price()) == float

    # Выводит текущее название ингридиента
    def test_get_name_ingredient_valid_name_true(self):
        ingredient = Ingredient('FILLING', 'Сыр с астероидной плесенью', 5.5)
        assert ingredient.get_name() == 'Сыр с астероидной плесенью' and type(ingredient.get_name()) == str

    # Выводит текущей тип ингридиента
    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_ingredient_valid_type_true(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'Сыр с астероидной плесенью', 5.5)
        assert ingredient.get_type() == ingredient_type and type(ingredient.get_type()) == str
