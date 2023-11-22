# --- Конкурентность и параллелизм ---

# import threading
#
# number_list = []
#
# while True:
#     user_input = input('Введите число, для выхода "q": ')
#     if user_input == "q":
#         break
#     try:
#         number_list.append(int(user_input))
#     except ValueError:
#         print("Вы ввели не число")
#
#
# def summ_of_elements(value):
#     if value:
#         list_summ = sum(value)
#         print(list_summ)
#     else:
#         print("Список пустой")
#
#
# def list_avg(value):
#     if value:
#         list_summ = sum(value)
#         print(list_summ / len(value))
#     else:
#         print("Список пустой")
#
#
# if __name__ == "__main__":
#     sum_threading = threading.Thread(target=summ_of_elements, args=(number_list,))
#     avg_threading = threading.Thread(target=list_avg, args=(number_list,))
#
#     sum_threading.start()
#     avg_threading.start()
#
#     sum_threading.join()
#     avg_threading.join()


import socket


def start_server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    print(f"Сервер ожидает на порту {host}:{port}")

    while True:
        conn, address = server_socket.accept()
        print(f"Соединение установлено с адресом {address}")

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Client {data=}")
            message = input("-> ")
            conn.send(message.encode())

        conn.close()
        print("Соединение закрыто")


if __name__ == "__main__":
    start_server()
