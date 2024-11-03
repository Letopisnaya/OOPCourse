import pytest

def test_category_1(category_1):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert category_1.products == [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
        {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
    ]
    assert category_1.count_category == 1
    assert category_1.count_products == 3


def test_category_2(category_2):
    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_2.products == [
        {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    ]
    assert category_2.count_category == 2
    assert category_2.count_products == 1


def test_category_3(category_3):
    assert category_3.name == "Мониторы"
    assert category_3.description == "Игровой монитор"
    assert category_3.products == [
        {"name": "Titan Army", "description": "Трехсторонний безрамочный дизайн", "price": 10499.0, "quantity": 8},
        {
            "name": "AOC",
            "description": "Четкая смена кадров без их зависания и смазывания изображения.",
            "price": 12499.0,
            "quantity": 10,
        },
    ]
    assert category_3.count_category == 3
    assert category_3.count_products == 2


def test_category_property(category_1):
    assert category_1.products == [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
        {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
    ]


def test_category_app(category_1, products_new):
    assert category_1.count_products == 3
    category_1.products = products_new
    assert category_1.count_products == 4


def test_total_products(category_01):
    assert str(category_01) == "Смартфоны, количество продуктов: 27 шт."


def test_category_app_error(category_1, products_new):
    with pytest.raises(TypeError):
        category_1.products = 1


def test_average_price(category_0):
    assert category_0.average_price() == 195000


def test_average_price_empty(category_empty):
    assert category_empty.average_price() == 0