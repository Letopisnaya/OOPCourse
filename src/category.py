from src.product import Product


class Category:
    name: str
    description: str
    products: list

    count_category = 0
    count_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.count_category += 1
        Category.count_products = len(self.__products)

    def __str__(self):
        total_products = 0
        for product in self.__products:
            total_products += product.quantity
        return f"{self.name}, количество продуктов: {total_products} шт."

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products_new: Product):
        if isinstance(products_new, Product):
            self.__products.append(products_new)
            Category.count_products += 1
        else:
            raise TypeError

    @property
    def products_list(self):
        products_list = ""
        for product in self.__products:
            products_list += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_list

    def average_price(self):
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0