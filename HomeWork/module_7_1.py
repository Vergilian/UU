class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    # def get_products(self):
    #     file = open(self.__file_name, 'r')
    #     catalog = file.read()
    #     file.close()
    #     return catalog

    def get_products(self):
        file = open(self.__file_name, 'r')
        data1 = file.read().splitlines()  # Получаем все строки из файла
        file.close()
        return data1

    # def add(self, *products):
    #     one_str = self.get_products()
    #     for i in products:
    #         if str(i) not in one_str:
    #             file = open(self.__file_name, 'a')
    #             file.write(f'{i}\n')
    #             file.close()
    #         else:
    #             print(f'Продукт {i.name} уже есть в магазине')

    def add(self, *products):
        data = self.get_products()
        for product in products:
            found = False
            for i, existing in enumerate(data):
                if existing.split(', ')[0] == product.name:
                    part = existing.split(', ')
                    new_weight = float(part[1]) + product.weight
                    part[1] = str(new_weight)
                    data[i] = ', '.join(part)
                    print(f"Продукт {product.name} уже был в магазине, его общий вес теперь равен {new_weight}")
                    found = True
                    break
            if not found:
                data.append(str(product))
                print(f'{product}')

        file = open(self.__file_name, 'w')
        for product in data:
            file.write(f'{product}\n')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Melon', 9.5, 'Vegetables')

# print(p2) # __str__

s1.add(p1, p2, p3, p4)

# print(s1.get_products())
