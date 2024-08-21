from praktikum.database import Database


class TestDatabase:

    # По умолчанию в базе данных три обьекта булочек
    def test_default_value_three_bun_object(self):
        database = Database()
        assert (database.buns[0].name == "black bun" and database.buns[0].price == 100
                and database.buns[1].name == "white bun" and database.buns[1].price == 200
                and database.buns[2].name == "red bun" and database.buns[2].price == 300)

    # По умолчанию в базе данных шесть обьектов ингридиентов
    def test_default_value_six_ingredients_object(self):
        database = Database()
        assert (database.ingredients[0].name == 'hot sauce' and database.ingredients[0].price == 100
                and database.ingredients[1].name == 'sour cream' and database.ingredients[1].price == 200
                and database.ingredients[2].name == 'chili sauce' and database.ingredients[2].price == 300
                and database.ingredients[3].name == 'cutlet' and database.ingredients[3].price == 100
                and database.ingredients[4].name == 'dinosaur' and database.ingredients[4].price == 200
                and database.ingredients[5].name == 'sausage' and database.ingredients[5].price == 300)

    # Вывести доступные булочки
    def test_available_buns_quantity_three(self):
        database = Database()
        assert len(database.available_buns()) == 3

    # Вывести доступные ингридиенты
    def test_available_ingredients_quantity_six(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
