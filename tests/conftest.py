import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


@pytest.fixture
def product_smart_1():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_smart_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_smart_3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category_01(product_smart_1, product_smart_2, product_smart_3):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [product_smart_1, product_smart_2, product_smart_3],
    )


@pytest.fixture
def category_1(product_smart_1, product_smart_2, product_smart_3):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    )


@pytest.fixture
def category_3():
    return Category(
        "Мониторы",
        "Игровой монитор",
        [
            {"name": "Titan Army", "description": "Трехсторонний безрамочный дизайн", "price": 10499.0, "quantity": 8},
            {
                "name": "AOC",
                "description": "Четкая смена кадров без их зависания и смазывания изображения.",
                "price": 12499.0,
                "quantity": 10,
            },
        ],
    )


@pytest.fixture
def product_1():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_2():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def products_new():
    return Product('45" QLED 4K', "Отличная фоновая подсветка", 133000.0, 5)


@pytest.fixture
def product_3():
    return Product('55" QLED 4K', "Фоновая подсветка", 0, 7)


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone3():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
