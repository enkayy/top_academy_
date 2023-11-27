# --- Паттерны проектирования (ООП) ---
# синглтон паттерн


class Singleton:  # все классы наследуются от класса object
    _instance = None

    def __new__(cls):  # принимает объект класса, а не селф
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls


def test_singleton_identify():
    singleton_1 = Singleton()
    singleton_2 = Singleton()

    assert singleton_1 is singleton_2, "Singleton instances are not same"


def test_singleton_state():
    singleton_1 = Singleton()
    singleton_1.data = "Singleton data"
    singleton_2 = Singleton()

    assert singleton_2.data == "Singleton data", "Singleton state is not share"


test_singleton_identify()
test_singleton_state()


class AbstractFactory:
    def create_product_a(self):
        raise NotImplemented


# class ConcreateFactory(AbstractFactory):
#
#     def create_product_a(self):
#         return ProductA1
#
# def test_concreate_factory_creation():
#
#
# def test_product_creation_by_factory():
#     factory = ConcreteFactory()
#
#     product_a = factory.create_product_a()
#     product_b = factory.create_product_b()
#
#     assert isinstance(product_a, ProductA1), 'ProductA is not created by ConcreateFactory'

# # доделать дома, ссылка на гитхаб скинут
# class Logger:
#     _instance = None
#
#     def __new__(cls):
#
#         if cls._instance is None:
#             cls._instance = super(Logger, cls).__new__(cls)
#
#         return cls._instance
#
#     def log(self, message):
#             where_to_log = input('Log to file or console: ')
#             if where_to_log == 'file':
#                 print(num_list)
#                 print(max(num_list))
#                 print(min(num_list))
#             elif where_to_log == 'console':
#                 file_path = input('Введите путь до файла: ')
#                 with open(file_path, 'w') as file:
#                     file.write(str(num_list))
#                     file.write(str(max_num))
#                     file.write(str(min_num))
#             else:
#                 print('Invalid input')


# Паттерн стратегия
# суть изменить стратегию класса
# Паттерн фасад -- объединяет несколько фун-ций в одну
# Форматирование текста pip3 install black
# black .
# git div/diff
#
# Лайфхак для дз в гитхабе
# Прототип через deepcopy
