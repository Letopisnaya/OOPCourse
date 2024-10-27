def test_product1(product_1):
    assert product_1.name == "Samsung Galaxy C23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_product2(product_2):
    assert product_2.name == '55" QLED 4K'
    assert product_2.description == "Фоновая подсветка"
    assert product_2.price == 123000.0
    assert product_2.quantity == 7


def test_new_product(product_2):
    assert product_2.name == '55" QLED 4K'
    assert product_2.description == "Фоновая подсветка"
    assert product_2.price == 123000.0
    assert product_2.quantity == 7


def test_str_product(product_1):
    assert str(product_1) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product(product_1, product_2):
    assert product_1 + product_2 == 1761000
