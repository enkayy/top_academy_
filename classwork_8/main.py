# # Задача от Никиты из литкода, где нужно найти сводный индекс
#
# # nums = [1, 7, 3, 6, 5, 6]
# nums = [2, 1, -1]
# pivot = -1
#
# for i in range(len(nums)):
#     # if len(nums[:i]) == len(nums[i + 1:]):  # Одинаковое кол-во с двух сторон от определенного индекса
#     if sum(nums[:i]) == sum(nums[i + 1:]):
#         pivot = i
#         break
# print(pivot)


import re

# text = 'milk how dogs python'

# match = re.search(r'\w{4}', text)  # r - чтобы создать шаблон search - поиск первого вхождения
# print(match.group())  # group возвращает одно слово

# matches = re.findall(r'\b\w{4,}\b', text)  # findall - ищет все вхождения
# print(matches)

# text = '1234 124 756 34 6 147'
#
# matches = re.findall(r'\b\d{3}\b', text)
# print(matches)

# dates = '10.12.2001 15/01/2004 14.02.14 18-05-2024'
#
# # matches = re.findall(r'\d\d\.\d{2}\.\d{4}', dates)
# matches = re.sub(r'\d\d\.\d{2}\.\d{4}', r'dd.mm.yyy', dates)  # Находит паттерн и меняет его на строку, которую задали
#
# print(matches)


# text = 'Stepa, Ivan; Markal, Caud'
#
# matches = re.split(r'[,;]', ''.join(text.split()))  # Разделяет текст по сивмолам, которые задали.
# # Также делим по пробелу и потом соединяем, чтобы список был без пробелов
# print(matches)


# tels = '+9126664565 +7 (912)6664523 +7 (999)-999-9999 +7 (999)-99-999-78'
#
# correct_num = re.findall(r'\+7\s\(\d{3}\)-\d\d-\d{3}-\d\d', tels)  # /s необязателен, можно просто пробел поставить
# print(correct_num)


# emails = 'testmail.ru test@mail.ru test123@mail.com test@mail!com'
#
# correct_emails = re.findall(r'\w+@\w{2,20}\.[a-z]{2,3}', emails)  # Можно написать [cruom0-5], ([cruom],[0-5])
# print(correct_emails)


# text = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
#        industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type
#        and scrambled it to make a type specimen book. It has survived not only five centuries, but also the
#        leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with
#        the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing
#        software like Aldus PageMaker including versions of Lorem Ipsum.
#        '''
#
# word_4 = re.findall(r'\b\w{4}\b', text)
# print(word_4)
#
# words = re.findall(r'\w+,', text)
# print(words)


# # Задача от Никиты про номера
#
# license_plates = 'А578АЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
#
# personal_plates = re.findall(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', license_plates)
# taxi_plates = re.findall(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', license_plates)
#
# print(personal_plates)
# print(taxi_plates)

# import requests
# url ='http://www.columbia.edu/~fdc/sample.html'
# response = requests.get(url)
#
# text = response.text
#
# text_h3 = re.findall(r'<h3 id="\w*">(.*)</h3>', text)
# # text_h3 = re.findall(r'<h3.*</h3>', text)
#
# print(text_h3)

text = '4567'

if re.match(r'\d{4}', text):  # match возвращает True/False
    print('ok')

# Сразу несколько номеров телефона через split







