import re
from pprint import pprint

data = {}


def email_check(email: str) -> bool:
    """
    Проверяет email на правильность написания
    :param email: str
    :return: bool
    """
    if re.match(r'\w+@\w{2,20}\.[rucom]{2,3}', email):
        return True
    print('Email написан неправильно, попробуйте снова!')
    return False


def add_data() -> None:  # можно было сделать проверку на номер и кабинетаб но будем считать, что вводится все правильно
    email = input('\nВведите email: ')
    email_check(email)
    data[email] = {}
    name = input('Введите ФИО: ')
    data[email]['ФИО'] = name
    tel = input('Введите номер телефона: ')
    data[email]['Номер телефона'] = tel
    position = input('Введите должность: ')
    data[email]['Должность'] = position
    office_number = input('Введите номер кабинета: ')
    data[email]['Номер кабинета'] = office_number
    skype = input('Введите skype: ')
    data[email]['Skype'] = skype


def change_data() -> None:

    email = input('\nВведите email сотрудника, у которого вы хотите поменять данные: ')
    email_check(email)
    if email in data.keys():
        while True:
            select = input('\nКакие данные вы хотите поменять?\n'
                           '(Email, ФИО, Телефон, Должность, Кабинет, skype, конец): ').lower()
            if select == 'email':
                new_email = input('Введите новый email: ')
                temporary_dict = data[email]
                data[new_email] = data.pop(email)
                data[new_email] = temporary_dict
                email = new_email
            elif select == 'фио':
                new_name = input('Введите новое ФИО: ')
                data[email]['ФИО'] = new_name
            elif select == 'телефон':
                new_tel = input('Введите новый номер телефона: ')
                data[email]['Номер телефона'] = new_tel
            elif select == 'должность':
                new_position = input('Введите новую должность: ')
                data[email]['Должность'] = new_position
            elif select == 'кабинет':
                new_position = input('Введите новый номер кабинета: ')
                data[email]['Номер кабинета'] = new_position
            elif select == 'skype':
                new_skype = input('Введите новый skype: ')
                data[email]['Skype'] = new_skype
            elif select == 'конец':
                return
    else:
        print('Сотрудник с таким email нет!')
        return


def del_data() -> None:
    email = input('Введите email сотрудника, данные которого вы хотите удалить: ')
    email_check(email)
    if email in data.keys():
        data.pop(email)
        print('Сотрудник удален!')
    else:
        print('Сотрудник с таким email нет!')
        return


def find_data() -> None:
    email = input('Введите email сотрудника, данные которого вы хотите посмотреть: ')
    email_check(email)
    if email in data.keys():
        print(data.get(email))
    else:
        print('Сотрудник с таким email нет!')
        return


def main():
    while True:
        choice = input('\n1 - Добавить данные о сотруднике\n'
                       '2 - Изменить данные сотрудника\n'  
                       '3 - Найти данные сотрудника\n'
                       '4 - Удалить данные сотрудника\n'
                       '5 - Посмотреть все данные\n'
                       '6 - Закончить выполнение программы -> ')
        if choice == '1':
            add_data()
        elif choice == '2':
            change_data()
        elif choice == '3':
            find_data()
        elif choice == '4':
            del_data()
        elif choice == '5':
            pprint(data)
        elif choice == '6':
            break
        else:
            print('Такой опции нет!')


main()
