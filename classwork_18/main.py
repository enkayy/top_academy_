# --- ООП ---

# class Point:
#
#     MIN_COORD = 0  # Если нам нужно константы, то можно записать и в сам класс
#     MAX_COORD = 100  # капсом пишутся значению, которые не меняются, или редко
#
#     def __init__(self, x, y):
#         # self.x = x
#         # self.y = y
#         self.set_coordinates(x, y)  # можно вызвать метод, чтобы задать координаты
#
#     # def set_square(self, left, right):
#     #     Point.MIN_COORD = left  # self меняет у одного экземпляра, а используя класс меняется сразу у всего класса
#     #     Point.MAX_COORD = right
#
#     @classmethod  # лучше делать так, чтобы при замене названия класса ничего не сломалось
#     def set_square(cls, left, right):  # срабатывает много раз __getattributе__, потому что тут cls, а не Point
#         cls.MIN_COORD = left  # self меняет у одного экземпляра, а используя класс меняется сразу у всего класса
#         cls.MAX_COORD = right
#
#     def set_coordinates(self, x, y):
#         if self.MIN_COORD <= x <= self.MAX_COORD and self.MIN_COORD <= y <= self.MAX_COORD:
#             self.x = x
#             self.y = y
#         else:
#             print('Точка лежит вне области!')
#
#     def __setattr__(self, key, value):  # срабатывает, когда меняется атрибут
#         print('Сработало __setattr__')
#         if key == 'w':
#             raise ValueError('Недопустипое значение атрибута')
#         object.__setattr__(self, key, value)
#
#     def __getattribute__(self, item):  # срабатывает когда вызываем метод или свойство атрибута
#
#         print('Сработал метод __getattribute__')
#         if item == 'x':  # можно написать, если мы не хотим, чтобы у пользователя был доступ к атрибуту
#             raise ValueError('У вас нет доступа к этому атрибуту')
#         return object.__getattribute__(self, item)
#
#     def __str__(self):
#         return f'Координаты точки: x = {self.x}, y = {self.y}'
#
#
# # print(Point.__dict__)  # Можно получить данные по классу
# #
# # point_1 = Point(20, 1)
# # point_1.MIN_COORD = 50
# # point_1.MAX_COORD = 150
# # print(point_1)
# # print(point_1.MIN_COORD)
# # print(point_1.MAX_COORD)
# #
# # point_2 = Point(2, 2)
# # print(point_2.MIN_COORD)
# # print(point_2.MAX_COORD)
#
# # point = Point(1, 2)
# # point.set_square(40, 80)
# # print(Point.__dict__)
# #
# # point_1 = Point(3, 4)
# # print(point.MIN_COORD, point_1.MAX_COORD)
#
# point = Point(1, 2)
# point.k = 5
#
# print(point.y)


# --- Наследование ---
# Один класс может наследовать данные другого

class Employee:

    ID = 0
    TAX = 0.13

    def __init__(self, email, salary):
        Employee.ID += 1
        self.id = Employee.ID
        self.email = email
        self.salary = salary

    def get_salary_for_month(self, bonus=0):
        return self.salary - self.salary * self.TAX + bonus  # налог + премия # Нужно брать налог у экземпляра класса
    # поэтому ставим self.TAX, а не Employee.TAX

    def __str__(self):
        return f'id: {self.id}\nemail: {self.email}\nsalary: {self.salary}\n'


# использование наследования


class Manager(Employee):  # наследоваться могут несколько классов
    TAX = 0.1  # можно переопределить значение в другом наследуемом классе

    def __init__(self, email, salary, employees):
        super(Manager, self).__init__(email, salary)
        self.employees = employees

    def get_employees(self):
        if self.employees:
            for i_employee in self.employees:
                print(f'\tid: {i_employee.id}\n\temail: {i_employee.email}\n\tsalary{i_employee.salary}\n')

    def __str__(self):
        return f'id: {self.id}\nemail: {self.email}\nsalary: {self.salary}\nEmployees: {self.employees}'
    # к работнику можно обратится через id и ключу email


class Engineer(Employee):

    TAX = 0.11
    RATE_PER_HOUR = 500

    def __init__(self, email, rank):
        super(Engineer, self).__init__(email, salary=0)
        self.rank = rank

    def get_salary_for_month(self, hours=0):
        self.salary = (self.RATE_PER_HOUR * hours) * (1 - self.TAX)
        return self.salary

    @classmethod
    def rub_per_hour(cls, per_hour):
        cls.RATE_PER_HOUR = per_hour

    def __str__(self):
        return f'id: {self.id}\nemail: {self.email}\nrank: {self.rank}\nsalary: {self.salary}\n'


engineer_1 = Engineer('engineer@mail.ru', 6)
engineer_1.rub_per_hour(4000)
engineer_1.get_salary_for_month(160)
print(engineer_1)


# employee_1 = Employee('set@mail.ru', 23000)
# employee_2 = Employee('test@mail.ru', 29000)
# # print(employee_1.get_salary_for_month(10000))
# # print(employee_2.get_salary_for_month(10000))
# print(employee_1)
# print(employee_2)
#
# manager_1 = Manager('boss@mail.ru', 90000, [employee_1, employee_2])
# # print(manager_1.get_salary_for_month())
# print(manager_1)
# manager_1.get_employees()
































