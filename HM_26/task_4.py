import os
import threading


def find_files(directory, search_word, output_file):
    files_with_word = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                if search_word in f.read():
                    files_with_word.append(file_path)

    with open(output_file, 'w') as output:
        for file_path in files_with_word:
            with open(file_path, 'r') as f:
                output.write(f.read())


def remove_forbidden_words(input_file, forbidden_words_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    with open(forbidden_words_file, 'r') as f:
        forbidden_words = f.read().splitlines()

    for word in forbidden_words:
        content = content.replace(word, '')

    with open(output_file, 'w') as f:
        f.write(content)


def main():
    directory = input("Введите путь к директории: ")
    search_word = input("Введите искомое слово: ")

    output_file = "merged_files.txt"
    thread1 = threading.Thread(target=find_files, args=(directory, search_word, output_file))
    thread1.start()

    thread1.join()

    forbidden_words_file = input("Введите путь к файлу с запрещенными словами: ")

    output_file2 = "result.txt"
    thread2 = threading.Thread(target=remove_forbidden_words, args=(output_file, forbidden_words_file, output_file2))
    thread2.start()

    thread2.join()

    print("Статистика:")
    print("Найдено файлов с искомым словом:", len(os.listdir(directory)))
    print("Объединенный файл создан:", output_file)
    print("Результат после удаления запрещенных слов сохранен в файле:", output_file2)


if __name__ == '__main__':
    main()
