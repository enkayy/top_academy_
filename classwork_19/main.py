# --- Магические методы ---

# class MyZeroDivisionError(ZeroDivisionError):  # Так создается собственная ошибку, которую можно залогировать в файл
#
#     def __init__(self, message=''):
#         self.message = message
#
#
# def divide(a, b):
#     # try:
#     #     return a / b
#     # except ZeroDivisionError:
#     #     raise MyZeroDivisionError
#     # except MyZeroDivisionError('Деление на ноль!') as error:
#     #     return error.message
#     #
#     try:
#         if b == 0:
#             raise MyZeroDivisionError('Деление на ноль!')
#     except MyZeroDivisionError as error:
#         return error
#
#
# print(divide(1, 0))


# class Vehicle:
#
#     def __init__(self, weight):
#         self.weight = weight
#
#
# class Ship(Vehicle):
#     pass
#
#
# base_vehicle = Vehicle(1000)
# ship = Ship(1000)
#
#
# print(isinstance(base_vehicle, Vehicle))  # является ли объект экземпляром класса
# print(isinstance(ship, Vehicle))  # является ли объект экземпляром класса
# print(issubclass(Ship, Vehicle))  # является ли подклассом


# class Multiply:
#
#     def __init__(self, num_1, num_2):
#         self.num_1 = num_1
#         self.num_2 = num_2
#
#     def __call__(self, *args, **kwargs):  # когда вызываешь экземпляр, как функцию срабатывает этот метод
#         print(f'Hi {kwargs["name"]}!')  # можно передавать что-то и получить доступ через кварги
#         return self.num_1 * self.num_2
#
#
# multiple = Multiply(10, 13)
# result = multiple(name='Smit')  # можно передавать и получить доступ через кварги
# print(result)


# # Перегрузка операторов (арифметических)
# # нужно, чтобы складывать число и объект класса или два объекта
#
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):  # перегрузка для +
        if isinstance(other, Number):
            return self.num + other.num  # складывается два экземпляра
            # если хотим сложить 3 объекта, то нужно вернуть объект, а не инт
            # и выводит резултат через св-во экземпляра
        else:
            return "Сложение невозможно"

    def __sub__(self, other):  # перегрузка для -
        if isinstance(other, Number):
            return Number(self.num - other.num)

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.num * other.num)

    def __divmod__(self, other):
        if isinstance(other, Number):
            return Number(self.num % other.num)

    def __truediv__(self, other):
        if isinstance(other, Number):
            return Number(self.num / other.num)

    def __eq__(self, other):  # сравнение
        if isinstance(other, Number):
            return self.num == other.num
        else:
            return "Сравнение невозможно"

    def __gt__(self, other):  # больше
        if isinstance(other, Number):
            return self.num > other.num
        else:
            return "Сравнение невозможно"

    def __ge__(self, other):  # больше или равно
        if isinstance(other, Number):
            return self.num >= other.num
        else:
            return "Сравнение невозможно"

    def __lt__(self, other):  # меньше
        if isinstance(other, Number):
            return self.num < other.num
        else:
            return "Сравнение невозможно"

    def __le__(self, other):  # меньше или равно
        if isinstance(other, Number):
            return self.num <= other.num
        else:
            return "Сравнение невозможно"

    def __ne__(self, other):  # неравно
        if isinstance(other, Number):
            return self.num != other.num
        else:
            return "Сравнение невозможно"


number_1 = Number(10)
number_2 = Number(10)
print(number_1 != number_2)

result = number_1 / number_2
print(result.num)


# # Корзина на сайте
#
# class Product:
#
#     def __init__(self, name, price, quantity, shop, discount=0):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.shop = shop
#         self.discount = discount
#
#     def get_total_product_price(self):
#
#         return self.price * (1 - self.discount * 0.01) * self.quantity
#
#
# class Shop:
#
#     def __init__(self, name):
#         self.name = name
#
#
# class Cart:
#
#     def __init__(self):
#         self.cart = []
#
#     def __add__(self, other):
#         if isinstance(other, Cart):
#             # merge_cart = Cart()  # первый способ
#             # merge_cart.cart = self.cart + other.cart
#             # return merge_cart
#             self.cart += other.cart
#             return self
#         return 'Невозможно произвести слияние корзин!'
#
#     def add_product(self, *args):
#         for i_product in args:
#             self.cart.append(i_product)
#
#     def get_all_products_in_cart(self):
#         print('\nТовары в корзине:')
#         for i_product in self.cart:
#             print(f'Название: {i_product.name}\n'
#                   f'\tМагазин: {i_product.shop.name}\n'  # тут получаем экземпляр класса shop, поэтому пишем еще name
#                   f'\tЦена: {i_product.price}\n'
#                   f'\tКол-во: {i_product.quantity}\n'
#                   f'\tСкидка: {i_product.discount}%\n'
#                   f'\tОбщая стоимость: {i_product.get_total_product_price()}\n'  # при вызове метода нужн круглые скобки
#                   f'{"":-^25}')
#         print(f'Общая стоимость товара в корзине: {self.total_cart_amount()}')
#
#     def total_cart_amount(self):
#         total_price = sum([i_product.get_total_product_price()
#                           for i_product in self.cart])
#         return total_price
#
#
# shop_1 = Shop('Magnit')
# shop_2 = Shop('Monetka')
#
#
# cart_1 = Cart()
# cart_1.add_product(Product('Apple', 100, 5, shop_1, 15), Product('Banana', 200, 8, shop_2))
# # cart_1.get_all_products_in_cart()
#
#
# cart_2 = Cart()
# cart_2.add_product(Product('Fish', 500, 2, shop_1, 30), Product('Pork', 400, 1, shop_1))
# # cart_2.get_all_products_in_cart()
#
# cart_1 += cart_2
# cart_1.get_all_products_in_cart()
# del cart_2  # удаляем, потому что записываем в первую таблицу
#
# # cart_3 = cart_1 + cart_2  # Вариант 1
# # cart_3.get_all_products_in_cart()
