import random
import threading


def fill_list(lst):
    for _ in range(10):
        lst.append(random.randint(1, 100))


def calculate_sum(lst):
    total_sum = sum(lst)
    print("Сумма элементов списка:", total_sum)


def calculate_average(lst):
    average = sum(lst) / len(lst)
    print("Среднеарифметическое значение списка:", average)


def main():
    random_list = []
    lock1 = threading.Lock()
    lock2 = threading.Lock()

    thread1 = threading.Thread(target=fill_list, args=(random_list,))
    thread1.start()

    lock1.acquire()
    lock2.acquire()

    thread2 = threading.Thread(target=calculate_sum, args=(random_list,))
    thread2.start()

    thread3 = threading.Thread(target=calculate_average, args=(random_list,))
    thread3.start()

    thread1.join()

    lock1.release()
    lock2.release()

    thread2.join()
    thread3.join()

    print("Список:", random_list)


if __name__ == '__main__':
    main()

