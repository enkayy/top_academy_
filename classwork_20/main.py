# --- Структуры данных ---

# class Queue:  # Очередь
#
#     def __init__(self):
#         """
#         FIFO первый пришел, первый вышел (First in First out)
#         """
#         self.queue = []
#
#     def add_item(self, item):
#         self.queue.append(item)
#
#     def pop_item(self):
#         if self.queue:
#             self.queue.pop(0)
#
#     def show_queue(self):
#         print(f'Очередь: {self.queue}')
#         return self.queue
#
#
# queue_1 = Queue()
# queue_1.show_queue()
# queue_1.add_item(5)
# queue_1.add_item(6)
# queue_1.add_item(7)
# queue_1.show_queue()
# queue_1.pop_item()
# queue_1.show_queue()
# queue_1.pop_item()
# queue_1.show_queue()


# class Stack:
#     """
#     Last in First out LIFO, последний пришел, первый вышел
#     """
#     def __init__(self):
#         self.stack = []
#
#     def add_item(self, item):
#         self.stack.append(item)
#
#     def pop_item(self):
#         self.stack.pop()
#
#     def show_stack(self):
#         print(f'Очередь: {self.stack}')
#         return self.stack
#
#
# stack = Stack()
# stack.show_stack()
# stack.add_item(5)
# stack.add_item(6)
# stack.add_item(7)
# stack.show_stack()
# stack.pop_item()
# stack.show_stack()
# stack.pop_item()
# stack.show_stack()

# Библиотека Collections для Queue и stack

# Связанные списки, существуют еще двунаправленные списки

class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, head):
        self.head = head

    def get_all_nodes(self):
        current = self.head
        while current:
            # print(current.value)
            # можно сделать генератор, написав yield current.values
            yield current.value
            current = current.next

    def remove_node(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def get_nodes_number(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count

    def get_middle_node(self):
        current = self.head
        count = self.get_nodes_number()
        for _ in range(count // 2):
            current = current.next
        return current.value

    def get_node_by_num(self, node_num):
        current = self.head
        for _ in range(node_num):
            current = current.next
        return current.value

    def change_head_node(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


head = Node(1)  # Головной узел

node_1 = Node(2)  # Первый узел
head.next = node_1  # присвоить ссылку на следующий элемент

node_2 = Node(3)
node_1.next = node_2

node_3 = Node(4)
node_2.next = node_3

node_4 = Node(5)
node_3.next = node_4

linked_list = LinkedList(head)
# linked_list.get_all_nodes()

# linked_list.remove_node(3)

# for i in linked_list.get_all_nodes():
#     print(i)

# 1 посчитать сколько всего узлов, включая головной
# print(linked_list.get_nodes_number())

# 2 найти серединный узел
# print(linked_list.get_middle_node())

# print(linked_list.get_node_by_num(4))

# linked_list.change_head_node(22)

linked_list.reverse()

for i in linked_list.get_all_nodes():
    print(i)



















































