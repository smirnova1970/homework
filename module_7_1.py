from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        str_products = f'{self.name}, {self.weight}, {self.category} '
        return str_products


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return str(products)

    def add(self, *products):
        file = open(self.__file_name, 'a')
        new_products = self.get_products()
        for product in products:
            if new_products.find(f'{product.name},') == -1:
                file.write(str(product) + '\n')
                new_products += product.name 
            else:
                print(f'Продукт {product.name} уже есть в магазине.')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)      # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
