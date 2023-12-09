import random
import threading


def fill_file_with_random_numbers(file_path, num_numbers):
    with open(file_path, 'w') as file:
        for _ in range(num_numbers):
            file.write(str(random.randint(1, 20)) + '\n')


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(file_path, output_path):
    primes = []
    with open(file_path, 'r') as file:
        for line in file:
            num = int(line.strip())
            if is_prime(num):
                primes.append(num)
    with open(output_path, 'w') as file:
        for prime in primes:
            file.write(str(prime) + '\n')


def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def calculate_factorial(file_path, output_path):
    factorials = []

    with open(file_path, 'r') as file:
        for line in file:
            num = int(line.strip())
            result = 1
            for i in range(1, num + 1):
                result *= i
            factorial_num = result
            factorials.append(factorial_num)
    with open(output_path, 'w') as file:
        for factorial in factorials:
            file.write(str(factorial) + '\n')


def main():
    file_path = input('Введите путь к файлу: ')
    num_numbers = 10

    fill_thread = threading.Thread(target=fill_file_with_random_numbers, args=(file_path, num_numbers))
    fill_thread.start()
    fill_thread.join()

    prime_output_path = 'primes.txt'
    factorial_output_path = 'factorials.txt'

    prime_thread = threading.Thread(target=find_primes, args=(file_path, prime_output_path))
    factorial_thread = threading.Thread(target=calculate_factorial, args=(file_path, factorial_output_path))
    prime_thread.start()
    factorial_thread.start()

    prime_thread.join()
    factorial_thread.join()

    print('Статистика выполненных операций:')
    print(f'Найдено простых чисел: {sum(1 for _ in open(prime_output_path))}')
    print(f'Рассчитано факториалов: {sum(1 for _ in open(factorial_output_path))}')


if __name__ == '__main__':
    main()
