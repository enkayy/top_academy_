import re

# phone_numbers_list = ['9999999999', '999999-999', '8999989999']  # Вариант, когда на вход подается список

phone_numbers = '9999999999 999999-999 8999989999'  # Вариант, когда на входе строка
phone_numbers_list = phone_numbers.split(' ')

count = 0

for i_phone in phone_numbers_list:
    count += 1
    if re.match(r'9\d{9}', i_phone) or re.match(r'8\d{9}', i_phone):
        print(f'{count} номер: все в порядке')
    else:
        print(f'{count} номер: не подходит')



