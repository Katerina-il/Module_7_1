from pprint import pprint

"""
Домашнее задание по теме "Режимы открытия файлов"

Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.
Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.

"""

class Product:
    """
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и
обладать следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
Все данные в строке разделены запятой с пробелами.

    """
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
        self.new_name = f"{self.name}, {self.weight}, {self.category}"

    def __str__(self):
        self.str = f"{self.name}, {self.weight}, {self.category}"
        return f"{self.name}, {self.weight}, {self.category}"



class Shop:
    """
Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product. Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .


    """


    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        open_file = open(self.__file_name, 'r')
        base_file = open_file.read()
        open_file.close()
        return base_file

    def add(self, *products):

        for product in products:
            open_file = open(self.__file_name, 'r')
            base_file = open_file.read()
            write_file = open (self.__file_name, 'a')
            # seek = 0
            if not product.new_name in base_file:
                #write_file.seek (seek)
                write_file.write (f'{product.__str__ ()} \n')
                # seek += len(product.__str__()) + 4
                write_file.close ()
                continue
            else:
                print (f'Продукт {product.name} уже есть в магазине')
                open_file.close ()
            continue



            # Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')



print(p2) # __str__
s1.add(p1, p2, p3)

print(s1.get_products())

