# # Задание 1
#
# class Node:
#
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
# class LinkedList:
#
#     def __init__(self, head):
#         self.head = head
#
#     def add_node(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#
#     def remove_node(self, value):
#         if self.head.value == value:
#             self.head = self.head.next
#             return
#
#         current = self.head
#         prev = None
#         while current:
#             if current.value == value:
#                 prev.next = current.next
#                 return
#             prev = current
#             current = current.next
#
#     def get_all_nodes(self):
#         current = self.head
#         while current:
#             print(current.value, end=' ')
#             current = current.next
#         print('')
#
#     def check_num_in_list(self, value):
#         current = self.head
#         while current:
#             if current.value == value:
#                 print(f'Значение "{value}" в списке есть')
#                 return True
#             current = current.next
#         print(f'Значения "{value}" в списке нет')
#         return False
#
#     def change_node(self, old_value, new_value):
#         current = self.head
#         while current:
#             if current.value == old_value:
#                 current.value = new_value
#                 return
#             current = current.next
#
#
# head = Node(0)
#
# node_1 = Node(1)
# head.next = node_1
#
# node_2 = Node(2)
# node_1.next = node_2
#
# linked_list = LinkedList(head)
#
#
# def menu():
#     while True:
#         choice = input('\n1 - Добавить элемент в список.\n'
#                        '2 - Удалить элемент из списка.\n'
#                        '3 - Показать содержимое списка.\n'
#                        '4 - Проверить есть ли значение в списке.\n'
#                        '5 - Заменить значение в списке.\n'
#                        '6 - Закончить ------> ')
#         if choice == '1':
#             value = int(input('\nВведите значение для добавления: '))
#             linked_list.add_node(value)
#         elif choice == '2':
#             value = int(input('\nВведите значение для удаления: '))
#             linked_list.remove_node(value)
#         elif choice == '3':
#             linked_list.get_all_nodes()
#         elif choice == '4':
#             value = int(input('\nВведите значение для проверки: '))
#             linked_list.check_num_in_list(value)
#         elif choice == '5':
#             old_value = int(input('\nВведите старое значение для замены: '))
#             new_value = int(input('Введите новое значение: '))
#             linked_list.change_node(old_value, new_value)
#         elif choice == '6':
#             print('\nЗавершение работы...')
#             break
#         else:
#             print('\nТакого функции нет!')
#
#
# menu()


# # Задание 2
#
# class Node:
#
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev
#
#
# class LinkedList:
#
#     def __init__(self, head):
#         self.head = head
#
#     def add_node(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             new_node.prev = current
#             current.next = new_node
#
#     def remove_node(self, value):
#         if self.head.value == value:
#             self.head = self.head.next
#             return
#
#         current = self.head
#         prev_node = None
#         while current:
#             if current.value == value:
#                 prev_node.next = current.next
#                 current.prev = prev_node
#                 return
#             prev_node = current
#             current = current.next
#
#     def get_all_nodes(self):
#         current = self.head
#         while current:
#             print(current.value, end=' ')
#             current = current.next
#         print('')
#
#     def check_num_in_list(self, value):
#         current = self.head
#         while current:
#             if current.value == value:
#                 print(f'Значение "{value}" в списке есть')
#                 return True
#             current = current.next
#         print(f'Значения "{value}" в списке нет')
#         return False
#
#     def change_node(self, old_value, new_value):
#         current = self.head
#         while current:
#             if current.value == old_value:
#                 current.value = new_value
#                 return
#             current = current.next
#
#
# head = Node(0)
#
# node_1 = Node(1)
# head.next = node_1
# node_1.prev = head
#
# node_2 = Node(2)
# node_1.next = node_2
# node_2.prev = node_1
#
# linked_list = LinkedList(head)
#
#
# def menu():
#     while True:
#         choice = input('\n1 - Добавить элемент в список.\n'
#                        '2 - Удалить элемент из списка.\n'
#                        '3 - Показать содержимое списка.\n'
#                        '4 - Проверить есть ли значение в списке.\n'
#                        '5 - Заменить значение в списке.\n'
#                        '6 - Закончить ------> ')
#         if choice == '1':
#             value = int(input('\nВведите значение для добавления: '))
#             linked_list.add_node(value)
#         elif choice == '2':
#             value = int(input('\nВведите значение для удаления: '))
#             linked_list.remove_node(value)
#         elif choice == '3':
#             linked_list.get_all_nodes()
#         elif choice == '4':
#             value = int(input('\nВведите значение для проверки: '))
#             linked_list.check_num_in_list(value)
#         elif choice == '5':
#             old_value = int(input('\nВведите старое значение для замены: '))
#             new_value = int(input('Введите новое значение: '))
#             linked_list.change_node(old_value, new_value)
#         elif choice == '6':
#             print('\nЗавершение работы...')
#             break
#         else:
#             print('\nТакого функции нет!')
#
#
# menu()


# Задание 3

class Stack:

    def __init__(self, size):
        self.stack = []
        self.size = size
        # Реализация 4 задания - убрать размер размер стека, который мы вводим и убрать проверку на размер
        # при добавлении нового элемента

    def add(self, item):
        if len(self.stack) >= self.size:
            print('Стек переполнен!')
        else:
            self.stack.append(item)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def show_stack(self):
        print(f'Очередь: {self.stack}')

    def count(self):
        return len(self.stack)

    def check_is_empty(self):
        return len(self.stack) == 0

    def check_is_full(self):
        return len(self.stack) == self.size

    def clear(self):
        self.stack = []
        print("Стек очищен")

    def choice(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Стек пустой")
            return None


def main():
    stack = Stack(3)
    while True:
        choice = input('\n1 - Добавить значение в стек\n'
                       '2 - Удалить значение из стека\n'
                       '3 - Количество значений в стеке\n'
                       '4 - Проверить, пустой ли стек\n'
                       '5 - Проверить, полный ли стек\n'
                       '6 - Очистить стек\n'
                       '7 - Получить значение верхнего элемента стека без удаления\n'
                       '8 - Показать все значения стека\n'
                       '0 - Выход -----> ')

        if choice == '1':
            value = int(input('\nВведите значение: '))
            stack.add(value)

        elif choice == '2':
            stack.pop()

        elif choice == '3':
            count = stack.count()
            print(f'\nКоличество значений в стеке: {count}')

        elif choice == "4":
            if stack.check_is_empty():
                print('\nСтек пустой')
            else:
                print('\nСтек не пустой')

        elif choice == '5':
            if stack.check_is_full():
                print('\nСтек полный')
            else:
                print('\nСтек не полный')

        elif choice == '6':
            stack.clear()

        elif choice == '7':
            value = stack.choice()
            if value is not None:
                print(f'\nЗначение верхнего элемента стека: {value}')

        elif choice == '8':
            stack.show_stack()

        elif choice == '0':
            print('\nЗавершение работы...')
            break
        else:
            print('\nТакого варианта нет!')

main()