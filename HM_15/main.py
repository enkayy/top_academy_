with open("text.txt", "r", encoding="utf-8") as file:
    with open("stats.txt", "w") as stats_file:
        text = file.read()
        stats_file.write(
            f"Статистика по файлу:\n\nКол-во символов с пробелами: {len(text)}\n"
        )  # кол-во символов
        stats_file.write(
            f'Кол-во символов без пробелов: {len(text.replace(" ", ""))}\n'
        )  # кол-во символов без пробелов

        file.seek(0)
        lines = len(file.readlines())  # кол-во строк
        stats_file.write(f"Кол-во строк: {lines}\n")
        lines_2 = (
            text.count("\n") + 1
        )  # второй способ реализации кол-ва символов через текст файла
        stats_file.write(f"Кол-во строк: {lines_2} (второй способ)\n")

        count_vowel = 0
        for i_vowel in text.lower():
            if i_vowel in "аиеёоуыэюя":
                count_vowel += 1
        stats_file.write(f"Кол-во гласных: {count_vowel}\n")

        count_consonant = 0
        for i_consonant in text.lower():
            if i_consonant in "бвгдйжзклмнпрстфхцчшщ":
                count_consonant += 1
        stats_file.write(f"Кол-во согласных: {count_consonant}\n")

        count_nums = 0
        for i_num in text:
            # if i_num in '1234567890':  # можно посчитать двумя способами
            if i_num.isnumeric():
                count_nums += 1
        stats_file.write(f"Кол-во цифр: {count_nums}\n")
