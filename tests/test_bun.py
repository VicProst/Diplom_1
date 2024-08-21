from praktikum.bun import Bun


class TestBun:

    # По умолчанию название булки - 'Crunchie bun'
    def test_name_of_bun_valid_name_true(self):
        bun = Bun('Crunchie bun', 12.5)
        assert bun.name == 'Crunchie bun' and type(bun.name) == str

    # По умолчанию цена булки - 12.5
    def test_price_of_bun_valid_price_true(self):
        bun = Bun('Crunchie bun', 12.5)
        assert bun.price == 12.5 and type(bun.price) == float

    # Выводит текущее название булки
    def test_get_name_bun_valid_name_true(self):
        bun = Bun('Poppy bun', 9.5)
        assert bun.get_name() == 'Poppy bun' and type(bun.get_name()) == str

    # Выводит текущую цену булки
    def test_get_price_bun_valid_price_true(self):
        bun = Bun('Poppy bun', 9.5)
        assert bun.get_price() == 9.5 and type(bun.get_price()) == float
